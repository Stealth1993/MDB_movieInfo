# 🎬 Movie Info Application

## 🌟 Overview
Unlock the world of cinema with this sleek Python-powered application! Using Tkinter for the interface and IMDb Cinemagoer for data retrieval, this app helps you explore movie details effortlessly. Just type a movie name, pick the right match, and get instant details like title, year, rating, genres, directors, cast, plot summary, runtime, country, and language. Plus, see the movie's official poster with a single click! 🍿

## 🚀 Features
- 🔍 **Search movies** by name
- 📌 **Choose from multiple results** for accuracy
- 🎭 **View complete movie details** in a pop-up window
- 🖼️ **Open movie posters** in your web browser
- 🛠️ **Lightweight & user-friendly design**

## 📌 Requirements
- 🐍 Python 3.x
- 📦 `tkinter` (comes with Python)
- 🎞️ `imdbpy` (install via `pip install imdbpy`)

## 🛠️ Installation & Setup
1. 📥 Clone this repository or download the script.
2. 🛠️ Install dependencies by running:
   ```sh
   pip install imdbpy
   ```

## 🎬 How to Use
1. 🏃 Run the script:
   ```sh
   python movie_info.py
   ```
2. 🎤 Enter a movie name when prompted.
3. 🎯 Select the correct movie from the search results.
4. 📜 View all the juicy details in a pop-up window.
5. 🖼️ If available, the movie poster opens in your default browser!

## 🎭 Create an Executable (Windows)
Want a one-click experience? Convert your script into a standalone app:
```sh
pyinstaller --onefile --windowed --noconsole --icon=movie.ico movie_info.py
```

## 🔔 Notes
- Uses IMDb Cinemagoer (`imdbpy`) for fetching movie data.
- If you prefer a minimal version, disable browser interaction for poster display.

## 📜 License
This project is open-source and free to use, modify, and share! 🏆✨

📩 Have feedback or feature requests? Let’s chat! 🎉

