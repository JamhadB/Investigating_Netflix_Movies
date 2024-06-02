# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter data to the 1990s
movies_1990s = netflix_df[(netflix_df['type'] == 'Movie') & (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]

# Determine the most frequent movie duration in the 1990s
most_common_duration = movies_1990s['duration'].mode()[0]
duration = int(most_common_duration)
print("Most frequent movie duration in the 1990s:", duration)

# Identify short action movies (less than 90 minutes) from the 1990s and count them
short_action_movies = movies_1990s[(movies_1990s['duration'] < 90) & (movies_1990s['genre'] == 'Action')]
short_movie_count = len(short_action_movies)
print("Number of short action movies in the 1990s:", short_movie_count)