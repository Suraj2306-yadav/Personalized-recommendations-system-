import random

# Sample data for demonstration: User preferences
users = {
    "user1": {"action": 5, "comedy": 3, "drama": 2},
    "user2": {"action": 4, "comedy": 5, "drama": 3},
    "user3": {"action": 1, "comedy": 2, "drama": 5},
}

# Sample movies data
movies = {
    "movie1": {"action": 5, "comedy": 1, "drama": 2},
    "movie2": {"action": 4, "comedy": 4, "drama": 1},
    "movie3": {"action": 2, "comedy": 5, "drama": 3},
    "movie4": {"action": 3, "comedy": 2, "drama": 5},
}

# Function to recommend movies based on user preferences
def recommend_movies(user_id):
    if user_id not in users:
        return "User not found."

    user_preferences = users[user_id]
    recommendations = {}

    for movie, movie_genres in movies.items():
        score = 0
        for genre, rating in user_preferences.items():
            if genre in movie_genres:
                score += movie_genres[genre] * rating
        recommendations[movie] = score

    recommended_movie = max(recommendations, key=recommendations.get)
    return f"Recommended movie for {user_id}: {recommended_movie}"

# Example usage
user_input = input("Enter user ID (e.g., user1, user2, user3): ")
print(recommend_movies(user_input))
