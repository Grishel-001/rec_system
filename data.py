# A dictionary where keys are movie titles and values are a list of genres.
MOVIE_GENRES = {
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "The Shawshank Redemption": ["Drama"],
    "Goodfellas": ["Biography", "Crime", "Drama"],
    "Spirited Away": ["Animation", "Adventure", "Family"],
    "Your Name": ["Animation", "Drama", "Fantasy"],
    "Coco": ["Animation", "Adventure", "Family"],
    "Toy Story": ["Animation", "Adventure", "Comedy"],
    "The Godfather": ["Crime", "Drama"],
    "Se7en": ["Crime", "Drama", "Mystery"],
}

# --- Collaborative Filtering Data ---
# A nested dictionary where keys are usernames, and values are dictionaries
# of movie titles and their 1-5 star ratings.
USER_RATINGS = {
    "Alice": {
        "The Dark Knight": 5,
        "Inception": 5,
        "Interstellar": 4,
        "The Matrix": 5,
    },
    "Bob": {
        "The Dark Knight": 5,
        "Inception": 4,
        "Interstellar": 3,
        "Pulp Fiction": 4,
    },
    "Charlie": {
        "Pulp Fiction": 5,
        "Forrest Gump": 4,
        "The Shawshank Redemption": 5,
        "Goodfellas": 4,
    },
    "David": {
        "Pulp Fiction": 5,
        "The Shawshank Redemption": 5,
        "The Godfather": 4,
        "Se7en": 3,
    },
    "Eve": {
        "Spirited Away": 5,
        "Your Name": 4,
        "Coco": 5,
        "Toy Story": 3,
    },
    "Frank": {
        "Spirited Away": 4,
        "Coco": 5,
        "Toy Story": 4,
        "The Matrix": 3, # Frank likes animation and one sci-fi movie
    }
}