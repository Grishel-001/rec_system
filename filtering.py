def _jaccard_similarity(set1, set2):
    """
    Calculates the Jaccard similarity between two sets.
    Jaccard Similarity = (Size of Intersection) / (Size of Union)
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    return intersection / union if union > 0 else 0

def recommend_movies(target_user, all_user_ratings, num_recommendations=5):
    """
    Recommends movies to a target user based on ratings from similar users.

    Args:
        target_user (str): The username of the user to recommend for.
        all_user_ratings (dict): The nested dictionary of all user ratings.
        num_recommendations (int): The number of movies to recommend.

    Returns:
        list: A sorted list of (movie_title, predicted_score) tuples.
    """
    if target_user not in all_user_ratings:
        print(f"Error: User '{target_user}' not found in ratings data.")
        return []

    target_user_movies = set(all_user_ratings[target_user].keys())
    
    # 1. Find similar users
    user_similarities = []
    for user in all_user_ratings:
        if user == target_user:
            continue
        
        other_user_movies = set(all_user_ratings[user].keys())
        
        # We use Jaccard similarity on the *set of movies rated*
        # to find users with similar viewing habits.
        similarity = _jaccard_similarity(target_user_movies, other_user_movies)
        
        if similarity > 0:
            user_similarities.append((similarity, user))

    # Sort by similarity, highest first
    user_similarities.sort(reverse=True)

    if not user_similarities:
        print(f"Could not find any users similar to '{target_user}'.")
        return []

    # 2. Score items from similar users
    # We use a weighted average. Score = SUM(similarity * rating) / SUM(similarity)
    
    recommendation_scores = {}
    total_similarity = {}

    for similarity, user in user_similarities:
        for movie, rating in all_user_ratings[user].items():
            # Only recommend movies the target user hasn't seen
            if movie not in target_user_movies:
                # Add to the weighted score
                recommendation_scores[movie] = recommendation_scores.get(movie, 0) + rating * similarity
                # Keep track of the total similarity for normalization
                total_similarity[movie] = total_similarity.get(movie, 0) + similarity

    # 3. Normalize scores
    final_scores = []
    for movie, score in recommendation_scores.items():
        if total_similarity[movie] > 0:
            # Normalize the score
            final_scores.append((movie, score / total_similarity[movie]))

    # Sort by the final predicted score
    final_scores.sort(key=lambda item: item[1], reverse=True)

    return final_scores[:num_recommendations]