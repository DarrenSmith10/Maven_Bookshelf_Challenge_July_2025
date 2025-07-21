#Check data csv file for missing values and duplicates
import pandas as pd
def check_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    
    # Check for missing values
    missing_values = data.isnull().sum()
    
    # Check for duplicates
    duplicates = data.duplicated().sum()
    
    # Print the results
    print("Missing Values in Each Column:")
    print(missing_values[missing_values > 0])
    
    print("\nTotal Duplicates Found:", duplicates)
    return missing_values, duplicates
# Example usage
if __name__ == "__main__":
    file_path = 'goodreads_reviews.csv'  # Replace with your actual file path
    check_data(file_path)
# This code checks a CSV file for missing values and duplicates.
# It prints the number of missing values in each column and the total number of duplicate rows found
# in the dataset.
# Make sure to replace 'data.csv' with the actual path to your CSV file.
# This code is useful for data cleaning and preprocessing tasks in data analysis or machine learning projects.
# It helps ensure the quality of the dataset before further analysis or model training.
# This code is designed to check a CSV file for missing values and duplicates.
# It uses the pandas library to load the data and perform the checks.
# Ensure you have pandas installed in your environment
# by running `pip install pandas` if necessary.
# before running this script.
# Ensure you have pandas installed in your environment
 

#Now i want to clean the missing values and duplicates found
def clean_data(file_path, output_path):
    # Load the data
    data = pd.read_csv(file_path)
    
    # Drop rows with missing values
    data_cleaned = data.dropna()
    
    # Drop duplicate rows
    data_cleaned = data_cleaned.drop_duplicates()
    
    # Save the cleaned data to a new CSV file
    data_cleaned.to_csv(output_path, index=False)
    
    print("Data cleaned and saved to", output_path)
# Example usage
if __name__ == "__main__":
    file_path = 'goodreads_reviews.csv'  # Replace with your actual file path
    output_path = 'cleaned_goodreads_reviews.csv'  # Path to save the cleaned data
    clean_data(file_path, output_path)
# This code cleans the data by removing rows with missing values and duplicates.
# It saves the cleaned data to a new CSV file.
# Make sure to replace 'goodreads_works.csv' and 'cleaned_goodreads_works.csv' with your actual file paths.
# This is useful for preparing the dataset for further analysis or machine learning tasks.  
# Ensure you have pandas installed in your environment
# by running `pip install pandas` if necessary.