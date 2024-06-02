import pandas as pd

# Sample data
data = {
    "show_id": ["s1", "s2", "s3", "s4", "s5"],
    "type": ["Movie", "Movie", "Movie", "Movie", "Movie"],
    "title": ["Inception", "Toy Story", "The Irishman", "The Lion King", "Avengers: Endgame"],
    "director": ["Christopher Nolan", "John Lasseter", "Martin Scorsese", "Jon Favreau", "Anthony Russo"],
    "cast": ["Leonardo DiCaprio", "Tom Hanks", "Robert De Niro", "Donald Glover", "Robert Downey Jr."],
    "country": ["USA", "USA", "USA", "USA", "USA"],
    "date_added": ["September 1, 2021", "December 1, 2020", "November 27, 2019", "July 19, 2019", "April 26, 2019"],
    "release_year": [2010, 1995, 2019, 2019, 2019],
    "rating": ["PG-13", "G", "R", "PG", "PG-13"],
    "duration": [148, 81, 209, 118, 181],
    "genre": ["Action", "Children", "Drama", "Children", "Action"],
    "listed_in": ["Action & Adventure", "Children & Family Movies", "Dramas", "Children & Family Movies", "Action & Adventure"],
    "description": ["Thriller", "Comedy", "Critically Acclaimed Movies", "Musicals", "Blockbuster"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("netflix_data.csv", index=False)
