# Import the data from data.py
from data import MOVIE_GENRES, USER_RATINGS

# Import the recommender functions
import content_based
import filtering

def print_recommendations(title, recommendations):
    """Helper function to print recommendations neatly."""
    print(f"\n--- {title} ---")
    if not recommendations:
        print("No recommendations found.")
        return
        
    for i, (item, score) in enumerate(recommendations):
        print(f"{i+1}. {item} (Score: {score:.2f})")
    print("-" * (len(title) + 6))

def run_demos():
    """Runs demonstrations for both recommendation systems."""
    
    # --- Demo 1: Content-Based Filtering ---
    # User A likes 'The Dark Knight' and 'Inception'.
    # We expect recommendations for other Action/Sci-Fi/Drama movies.
    user_a_likes = ["The Dark Knight", "Inception"]
    
    content_recs = content_based.recommend_movies(
        user_liked_movies=user_a_likes,
        all_movie_genres=MOVIE_GENRES,
        num_recommendations=5
    )
    
    print_recommendations(
        f"Content-Based Recommendations (for user who likes {', '.join(user_a_likes)})",
        content_recs
    )

    # --- Demo 2: Collaborative Filtering ---
    # Target User is 'Alice'.
    # 'Alice' likes Action/Sci-Fi. 'Bob' is similar (likes Action/Sci-Fi).
    # 'Bob' also likes 'Pulp Fiction'.
    # We expect 'Pulp Fiction' to be recommended to 'Alice'.
    target_user_alice = "Alice"
    
    collab_recs_alice = filtering.recommend_movies(
        target_user=target_user_alice,
        all_user_ratings=USER_RATINGS,
        num_recommendations=5
    )
    
    print_recommendations(
        f"Collaborative Filtering Recommendations (for user '{target_user_alice}')",
        collab_recs_alice
    )
    
    # --- Demo 3: Collaborative Filtering (Animation) ---
    # Target User is 'Eve'.
    # 'Eve' likes animation. 'Frank' is similar (likes animation).
    # 'Frank' also likes 'The Matrix'.
    # We expect 'The Matrix' to be recommended to 'Eve'.
    target_user_eve = "Eve"
    
    collab_recs_eve = filtering.recommend_movies(
        target_user=target_user_eve,
        all_user_ratings=USER_RATINGS,
        num_recommendations=5
    )
    
    print_recommendations(
        f"Collaborative Filtering Recommendations (for user '{target_user_eve}')",
        collab_recs_eve
    )

if __name__ == "__main__":
    run_demos()