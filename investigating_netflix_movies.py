# Importing pandas and matplotlib
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Only selecting 90s movies -> netflix_90
netflix_90 = netflix_df[
    (netflix_df["release_year"] >= 1990) & 
    (netflix_df["release_year"] <= 1999) & 
    (netflix_df["type"] == "Movie")
]
duration = int(netflix_90["duration"].mode()[0])
print("Mode of duration (1990s movies): " + str(duration))

# Counting short movies
short_movie_count = netflix_90[
  (netflix_90["duration"] < 90) & 
  (netflix_90["genre"] == 'Action')
  ].shape[0]
print("Number of short action movies: " + str(short_movie_count))
