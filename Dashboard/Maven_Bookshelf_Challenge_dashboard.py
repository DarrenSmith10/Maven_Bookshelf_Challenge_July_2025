import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load your cleaned data (update filename if needed)
works_path = '../Clean_Data/cleaned_goodreads_works.csv'
reviews_path = '../Clean_Data/Final_cleaned_goodreads_reviews.csv'

if not os.path.exists(works_path):
	print(f"File not found: {works_path}")
else:
	works = pd.read_csv(works_path)  # Load the cleaned data

if not os.path.exists(reviews_path):
	print(f"File not found: {reviews_path}")
else:
	reviews = pd.read_csv(reviews_path)  # Load the cleaned reviews data


# Streamlit background colour

page_bg_img = """
<style>
body {
    background-color: rgb(56 67 90);
    font-family: 'Arial', sans-serif;
}
</style>
	
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Maven Bookshelf Dashboard")

# Genre selection
genres = works['genres'].dropna().unique()
genre = st.selectbox("Choose a genre", genres)

# Show top books in selected genre
top_books = works[works['genres'] == genre].sort_values('avg_rating', ascending=False).head(10)
st.subheader(f"Top 10 Books in {genre}")
st.dataframe(top_books[['original_title', 'author', 'avg_rating', 'original_publication_year']])

# Bar chart of average ratings
st.bar_chart(top_books.set_index('original_title')['avg_rating']) 

# Count of books by genre
fig, ax = plt.subplots()
sns.countplot(y='genres', data=works, order=works['genres'].value_counts().index[:10], ax=ax)
st.pyplot(fig)

# Visualize the distribution of average ratings
plt.figure(figsize=(10, 5))
sns.histplot(works['avg_rating'], bins=30, kde=True)
plt.title('Distribution of Average Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Frequency')
plt.show()

# Recommend top-rated books in a favorite genre
def recommend_books(genre, n=5):
    subset = works[works['genres'].str.contains(genre, case = False, na=False)]
    top_books = subset.sort_values('avg_rating', ascending=False).head(n)
    return top_books[['original_title', 'author', 'avg_rating', 'original_publication_year']]

st.subheader("Recommended Fantasy Books:")
st.dataframe(recommend_books('fantasy', 5))

# Show the number of books per genre
genre_counts = works['genres'].value_counts()
st.subheader("Number of Books per Genre")
st.bar_chart(genre_counts)
