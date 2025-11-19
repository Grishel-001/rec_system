# rec_system
# 🎬 Movie Recommendation System (Content-Based and Collaborative Filtering)

This repository contains a simple, yet effective, movie recommendation system built in Python. It demonstrates two fundamental approaches to recommendation: **Content-Based Filtering** (using movie genres) and **User-Based Collaborative Filtering** (using user ratings).

The system uses the **Jaccard Similarity** metric for calculating both movie-to-movie genre similarity and user-to-user rating commonality.

## 🌟 Features

* **Content-Based Filtering:** Recommends movies by matching the genres of a target user's liked movies to other movies in the catalog.
* **User-Based Collaborative Filtering:** Recommends movies to a target user by finding similar users (neighbors) and suggesting movies they rated highly but the target user hasn't seen.
* **Weighted Scoring:** Collaborative filtering uses a similarity-weighted average of ratings to predict a final score for unseen movies.
* **Modular Design:** Data, content-based logic, and filtering logic are separated into distinct modules (`data.py`, `content_based.py`, `filtering.py`).

## ⚙️ How It Works

### 1. Data (`data.py`)

Contains two main datasets:
* `MOVIE_GENRES`: A dictionary mapping movie titles to a list of genres (e.g., `["Action", "Sci-Fi"]`).
* `USER_RATINGS`: A nested dictionary of user-to-movie ratings (1-5 stars).

### 2. Content-Based Filtering (`content_based.py`)

This approach finds the **maximum genre overlap** between an unseen movie and *any* of the movies the user liked.

* **Similarity Metric:** Jaccard Similarity on the set of genres.
    $$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
* **Recommendation Logic:** For a given unseen movie, its score is the $\text{max}(\text{Jaccard Similarity})$ between its genre set and the genre set of every movie the user liked.

### 3. Collaborative Filtering (`filtering.py`)

This user-based approach relies on the principle that "users who agree in the past will agree in the future."

* **User Similarity:** Calculated using Jaccard Similarity on the *set of movies rated* by two users.
* **Prediction:** The predicted rating for an unseen movie is a **weighted average** of the ratings given by similar users (neighbors). The weights are the user similarities.
    $$\text{Score}_m = \frac{\sum_{u \in \text{Neighbors}} (\text{Sim}(\text{target}, u) \times \text{Rating}_{u, m})}{\sum_{u \in \text{Neighbors}} \text{Sim}(\text{target}, u)}$$



The `main.py` script will run the following demos and print the results:
* **Content-Based:** Recommendations for a user who likes action/sci-fi movies.
* **Collaborative (Alice):** Recommendations for a user based on similar action/sci-fi raters (like Bob).
* **Collaborative (Eve):** Recommendations for a user based on similar animation raters (like Frank).

