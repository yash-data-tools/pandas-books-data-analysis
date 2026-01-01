# Books Data Analysis with Pandas

This project performs data cleaning, filtering, and analysis on scraped book product data using **Pandas**.  
The goal is to transform raw, messy data into clean, structured, and analysis-ready datasets.

---

## Project Overview
The dataset used in this project comes from scraped book product data and contains information such as:
- Book title
- Price
- Availability
- Rating (text-based)
- Product links

Using Pandas, the data is cleaned, transformed, analyzed, and exported into multiple meaningful CSV outputs.

---

## Key Features
- Cleans raw scraped CSV data
- Converts price strings into numeric values
- Handles duplicate records
- Transforms text-based ratings into numeric values
- Filters high-value and high-rated products
- Performs groupby analysis with aggregation
- Exports multiple analysis-ready CSV files

---

## Technologies Used
- Python
- Pandas
- CSV

---

## Data Processing Steps
The script performs the following steps:
1. Loads raw book data from a CSV file
2. Inspects data structure and data types
3. Cleans and converts price values to numeric format
4. Removes duplicate records
5. Maps textual ratings (One–Five) to numeric values
6. Filters books based on price and rating conditions
7. Sorts filtered results
8. Generates aggregated statistics using groupby operations
9. Exports final datasets as CSV files

---

## Output Files
The project generates the following outputs:

- **Cleaned_data.csv**  
  Cleaned dataset with corrected data types and duplicates removed.

- **Filtered_items.csv**  
  Filtered list of books with high prices and high ratings.

- **Groupby_rating.csv**  
  Aggregated analysis showing book count and average price by rating.

---

## How to Run
1. Ensure Python is installed on your system
2. Install Pandas if not already installed: pip install pandas
3. Place the raw CSV file in the project directory
4. Run the script: python main.py
5. Check the generated CSV files in the project folder

---

## Use Cases
- Data cleaning and preprocessing
- Exploratory data analysis
- Preparing datasets for reporting or visualization
- Demonstrating Pandas skills for freelancing and portfolios

---

## Author
Yash Kumar Shaw

