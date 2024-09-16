import tkinter as tk
from tkinter import simpledialog, messagebox
from imdb import Cinemagoer

def get_movie_info():
    # Initialize the IMDb Cinemagoer object
    ia = Cinemagoer()

    # Hide the root Tkinter window (we don’t need it)
    root = tk.Tk()
    root.withdraw()

    # Ask the user for a movie name
    Movie = simpledialog.askstring("Movie Search", "Enter a movie name:")
    if not Movie:
        return

    # Search for the movie
    items = ia.search_movie(Movie)
    
    # Prepare search results for user selection
    result_text = "\nSearch results:\n"
    for index, movie in enumerate(items):
        title = movie.get('title', 'Unknown Title')
        year = movie.get('year', 'Unknown Year')
        result_text += f"{index + 1}. {title} ({year})\n"

    # Ask the user to select a movie from the list
    movie_index = simpledialog.askinteger("Select Movie", result_text + "\nEnter the number of the movie you want to get info for:")
    if movie_index is None or movie_index < 1 or movie_index > len(items):
        return
    movie_id = items[movie_index - 1].movieID

    # Get the selected movie's information
    movie_info = ia.get_movie(movie_id)

    # Format movie information
    info = (
        f"Title: {movie_info.get('title')}\n"
        f"Year: {movie_info.get('year')}\n"
        f"Rating: {movie_info.get('rating', 'N/A')}\n"
        f"Genres: {', '.join(movie_info.get('genres', []))}\n"
        f"Director(s): {', '.join(str(d) for d in movie_info.get('directors', []))}\n"
        f"Cast: {', '.join(str(c) for c in movie_info.get('cast', [])[:5])}...\n"
        f"Plot: {movie_info.get('plot outline', 'N/A')}\n"
        f"Runtime: {movie_info.get('runtimes', ['N/A'])[0]} minutes\n"
        f"Country: {', '.join(movie_info.get('countries', []))}\n"
        f"Language: {', '.join(movie_info.get('languages', []))}"
    )

    # Show the movie information in a message box
    messagebox.showinfo("Movie Information", info)

if __name__ == "__main__":
    get_movie_info()
