# Importing pandas
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter for 90s movies
netflix_90 = netflix_df[
    (netflix_df["release_year"].between(1990, 1999)) & 
    (netflix_df["type"] == "Movie")
]

# Mode of duration for 90s movies
duration = netflix_90["duration"].mode()[0]
print(f"Mode of duration (1990s movies): {duration} minutes")

# Count of short action movies (duration < 90 minutes)
short_movie_count = netflix_90[
    (netflix_90["duration"] < 90) & 
    (netflix_90["genre"] == 'Action')
].shape[0]
print(f"Number of short action movies: {short_movie_count}")
