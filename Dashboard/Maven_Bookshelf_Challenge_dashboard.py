import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from pathlib import Path
# Ensure the necessary directories exist

from pathlib import Path

from pathlib import Path

# # Load your cleaned data (update filename if needed) Old local way
# works_path = '../Clean_Data/cleaned_goodreads_works.csv'
# reviews_path = '../Clean_Data/Final_cleaned_goodreads_reviews.csv'

BASE = Path(__file__).parent  # folder where app.py lives
data_dir = BASE / "Clean_Data"
works_path = data_dir / "cleaned_goodreads_works.csv"
reviews_path = data_dir / "Final_cleaned_goodreads_reviews.csv"



if not os.path.exists(works_path):
	print(f"File not found: {works_path}")
else:
	works = pd.read_csv(works_path)  # Load the cleaned data

if not os.path.exists(reviews_path):
	print(f"File not found: {reviews_path}")
else:
	reviews = pd.read_csv(reviews_path)  # Load the cleaned reviews data


# Streamlit background colour
import streamlit as st

import streamlit as st

css_global = """
<style>
.stApp {
  background-image: linear-gradient(to bottom right, #010101, #393836);
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}
.stButton {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.stButton:hover {
  background-color: #45a049;
}
.stElementContainer {
  margin: 10px 0;
  color: bisque;
}

[data-testid="stHeader"], [data-testid="stToolbar"] {
  background: rgba(0,0,0,0);
}

</style>
"""
st.markdown(css_global, unsafe_allow_html=True)

# css_container = """
# <style>
# .st-key-my_blue_container {
#   background-color: rgba(100, 100, 255, 0.2);
#   padding: 1rem;
#   border-radius: 8px;
# }
# </style>
# """
# st.markdown(css_container, unsafe_allow_html=True)

# with st.container(key="my_blue_container"):
#     st.write("This container has custom styling")



#------ Cleaning the Genre # column and preparing the dataset for visualization ----
#Clean the Genres column
works['genres'] = works['genres'].str.split(',').str[0]  # Take the first genre if multiple are present
works['genres'] = works['genres'].str.strip()  # Remove leading/trailing whitespace
# Calculate average rating for each book
works['avg_rating'] = works['avg_rating'].astype(float)  # Ensure average_rating is float type
works['original_publication_year'] = works['original_publication_year'].astype(int)
# Ensure the 'genres' column is not empty
works = works[works['genres'].notna() & (works['genres'] != '')
]
# Remove rows with NaN in 'original_title' or 'author' 
works = works.dropna(subset=['original_title', 'author'])
# Remove duplicates based on 'original_title' and 'author'
works = works.drop_duplicates(subset=['original_title', 'author'])
# Display the first few rows of the dataset
st.subheader("Dataset Overview")

#--Genres selection and Recommendation ----------------------
#- Create a selectbox for genre selection
st.write("Select a genre to explore the top books and their ratings.")
# Genre selection
genres = works['genres'].dropna().unique()
genre = st.selectbox("Choose a genre", genres)


# Show top books in selected genre
top_books = works[works['genres'] == genre].sort_values('avg_rating', ascending=False).head(10)
st.subheader(f"Top 10 Books in {genre}")
st.dataframe(top_books[['original_title', 'author', 'avg_rating', 'original_publication_year']])

# Bar chart of average ratings with color
st.subheader(f"Average Ratings of Top 10 Books in {genre}")
fig_bar, ax_bar = plt.subplots(figsize=(8, 4))
sns.barplot(
    x='avg_rating',
    y='original_title',
    data=top_books,
    palette='viridis',
   
)
ax_bar.set_xlabel('Average Rating')
ax_bar.set_ylabel('Book Title')
st.pyplot(fig_bar)

# Recommend top-rated books in selected genre
st.subheader(f"Recommended Books in {genre}")
def recommend_books(genre, n=5):
    """Recommend top-rated books in a specific genre."""
    if genre not in works['genres'].values:
        st.error(f"No books found for genre: {genre}")
        return pd.DataFrame()  # Return an empty DataFrame if no books found

    # Filter works by genre and sort by average rating
    subset = works[works['genres'].str.contains(genre, case = False, na=False)]
    top_books = subset.sort_values('avg_rating', ascending=False).head(n)
    return top_books[['original_title', 'author', 'avg_rating', 'original_publication_year']]

st.dataframe(recommend_books(genre, 5))

#-- Caculate the total number of books in the dataset
st.write("This dataset contains a variety of books across different genres, with their average ratings and publication years.")
#-- Count of books by genre
st.subheader("Books by Genre")
# Count the number of books in each genre
genre_counts = works['genres'].value_counts().reset_index()
genre_counts.columns = ['genres', 'count']
# Display the count of books by genre
st.dataframe(genre_counts)
# Visualize the count of books by genre using seaborn
st.subheader("Visualization of Books by Genre")
# Set the figure size
plt.figure(figsize=(10, 6))
# Create a count plot for the top 10 genres
st.write("Top 10 Genres by Count")
plt.clf()  # Clear the current figure to avoid overlap in Streamlit
fig, ax = plt.subplots()
sns.countplot(
    y='genres',
    data=works,
    order=works['genres'].value_counts().index[:10],
    palette='mako',
    ax=ax
)
ax.set_xlabel('Number of Books')
ax.set_ylabel('Genre')
ax.set_title('Top 10 Genres by Book Count')
st.pyplot(fig)

# Display the total number of books in the dataset
st.subheader("Total Number of Books in the Dataset")
total_books = works.shape[0]
st.write(f"Total number of books: {total_books}")

#---- Visualize the distribution of average ratings ----
st.subheader("Distribution of Average Ratings")
fig_hist, ax_hist = plt.subplots(figsize=(10, 6))
sns.histplot(works['avg_rating'], bins=30, kde=True, color='#4F8BF9')
ax_hist.set_xlabel('Average Rating')
ax_hist.set_ylabel('Number of Books')
st.pyplot(fig_hist)






