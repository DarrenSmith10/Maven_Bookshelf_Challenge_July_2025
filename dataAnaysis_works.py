#take my cleaned data and use it to analyze the works using DF
import pandas as pd

df = pd.read_csv('cleaned_goodreads_works.csv')  # Load the cleaned data
print(df)



# def analyze_works(file_path):
#     # Load the cleaned data
#     data = pd.read_csv(file_path)
    
#     # Example analysis: Count the number of works by each author
#     author_counts = data['author'].value_counts()
    
#     # Print the results
#     print("Number of Works by Each Author:")
#     print(author_counts)
    
#     # Example analysis: Find the average rating of works
#     average_rating = data['avg_rating'].mean()
    
#     print("\nAverage Rating of Works:", average_rating)
    
#     return author_counts, average_rating
# # Example usage
# if __name__ == "__main__":
#     file_path = 'cleaned_goodreads_works.csv'  # Replace with your actual cleaned file path
#     analyze_works(file_path)
# # This code analyzes the cleaned data of works from a CSV file.
# # It counts the number of works by each author and calculates the average rating of the works.
# # Make sure to replace 'cleaned_goodreads_reviews.csv' with your actual cleaned file path.
# # This code is useful for gaining insights into the dataset after cleaning it.
# # It helps in understanding the distribution of works by authors and the overall quality of the works based on ratings.
# # Ensure you have pandas installed in your environment
# # by running `pip install pandas` if necessary.

