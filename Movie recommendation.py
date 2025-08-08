import tkinter as tk
from tkinter import messagebox

# Predefined list of movies with genre, rating, and description
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "description": "A mind-bending thriller about dreams within dreams."},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "description": "Batman faces off against the Joker."},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2, "description": "A powerful crime family drama."},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "description": "A man wrongfully imprisoned forms a lasting friendship with a fellow inmate."},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "description": "A space exploration film exploring love, sacrifice, and time."},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "description": "A computer hacker learns about the true nature of reality."},
    {"title": "The Lion King", "genre": "Animation", "rating": 8.5, "description": "A young lion prince must overcome adversity to reclaim his kingdom."},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "description": "A simple man leads an extraordinary life through historical events."},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4, "description": "The Avengers must undo the damage caused by Thanos."}
]

# Function to recommend movies based on selected genre
def recommend_movies():
    selected_genre = genre_var.get()
    
    # Filter movies based on genre
    filtered_movies = [movie for movie in movies if movie["genre"] == selected_genre]
    
    if not filtered_movies:
        messagebox.showinfo("No Recommendations", f"No movies found for {selected_genre} genre.")
        return
    
    # Clear previous recommendations
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    # Display the recommended movies
    for movie in filtered_movies:
        movie_title = movie["title"]
        movie_rating = movie["rating"]
        movie_description = movie["description"]
        
        # Display movie info
        tk.Label(result_frame, text=f"Title: {movie_title}", font=("Arial", 12, "bold"), bg='#ffeb3b', fg='#212121').pack(pady=5)
        tk.Label(result_frame, text=f"Rating: {movie_rating}", font=("Arial", 10), bg='#ffeb3b', fg='#212121').pack(pady=5)
        tk.Label(result_frame, text=f"Description: {movie_description}", font=("Arial", 10), wraplength=400, bg='#ffeb3b', fg='#212121').pack(pady=5)
        tk.Label(result_frame, text="-"*50, bg='#ffeb3b').pack(pady=10)  # Separator line

# Setting up the Tkinter window
window = tk.Tk()
window.title("Movie Recommendation System")
window.geometry("500x600")
window.config(bg="#1976D2")  # Background color of the main window

# Title label with color
title_label = tk.Label(window, text="Movie Recommendation System", font=("Arial", 18, "bold"), bg="#1976D2", fg="white")
title_label.pack(pady=20)

# Genre selection dropdown with custom styling
genre_var = tk.StringVar(value="Sci-Fi")  # Default genre
genres = ["Sci-Fi", "Action", "Crime", "Drama", "Animation"]
genre_label = tk.Label(window, text="Select Genre:", font=("Arial", 12), bg="#1976D2", fg="white")
genre_label.pack()

genre_menu = tk.OptionMenu(window, genre_var, *genres)
genre_menu.config(font=("Arial", 12), bg="#FF5722", fg="white", width=20)
genre_menu.pack(pady=10)

# Recommend button with color
recommend_button = tk.Button(window, text="Get Recommendations", font=("Arial", 12), command=recommend_movies, bg="#FF5722", fg="white", width=20)
recommend_button.pack(pady=20)

# Frame to display recommendations with a nice background color
result_frame = tk.Frame(window, bg='#ffeb3b')
result_frame.pack(pady=10, fill="both", expand=True)

# Run the Tkinter event loop
window.mainloop()
