def _jaccard_similarity(set1, set2):
    """
    Calculates the Jaccard similarity between two sets.
    Jaccard Similarity = (Size of Intersection) / (Size of Union)
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    return intersection / union if union > 0 else 0

def recommend_movies(user_liked_movies, all_movie_genres, num_recommendations=5):
    """
    Recommends movies based on genre similarity to the user's liked movies.

    Args:
        user_liked_movies (list): A list of movie titles the user likes.
        all_movie_genres (dict): A dictionary of all movies and their genres.
        num_recommendations (int): The number of movies to recommend.

    Returns:
        list: A sorted list of (movie_title, similarity_score) tuples.
    """
    if not user_liked_movies:
        return []

    # Convert the user's liked movies into sets of genres
    try:
        user_liked_genre_sets = [set(all_movie_genres[movie]) for movie in user_liked_movies]
    except KeyError as e:
        print(f"Error: Movie {e} not found in movie genres data.")
        return []

    # Find movies the user hasn't liked/seen yet
    unseen_movies = {movie: set(genres) for movie, genres in all_movie_genres.items() 
                     if movie not in user_liked_movies}

    # Calculate a score for each unseen movie
    recommendation_scores = []
    for movie, genres_set in unseen_movies.items():
        # The score is the *maximum* similarity to any of the user's liked movies
        score = max(_jaccard_similarity(genres_set, liked_set) for liked_set in user_liked_genre_sets)
        
        if score > 0:
            recommendation_scores.append((movie, score))

    # Sort recommendations by score in descending order
    recommendation_scores.sort(key=lambda item: item[1], reverse=True)
    
    return recommendation_scores[:num_recommendations]