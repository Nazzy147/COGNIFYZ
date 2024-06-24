#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Function to load dataset
def load_dataset(filepath):
    try:
        data = pd.read_csv(filepath)
        logging.info(f"Dataset loaded successfully from {filepath}")
        return data
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        return None

# Function to determine the most common price range
def most_common_price_range(data):
    common_price_range = data['Price range'].mode()[0]
    logging.info(f"Most Common Price Range: {common_price_range}")
    return common_price_range

# Function to calculate the average rating by price range
def calculate_avg_rating_by_price_range(data):
    avg_rating_by_price_range = data.groupby('Price range')['Aggregate rating'].mean().reset_index()
    avg_rating_by_price_range.columns = ['Price range', 'Average rating']
    logging.info("Average rating for each price range:\n" + str(avg_rating_by_price_range.round(2)))
    return avg_rating_by_price_range

# Function to visualize average rating by price range
def visualize_avg_rating_by_price_range(avg_rating_by_price_range):
    highest_avg_rating_index = avg_rating_by_price_range['Average rating'].idxmax()
    
    plt.figure(figsize=(12, 7))
    sns.set(style="whitegrid")
    colors = ['red' if i == highest_avg_rating_index else 'blue' for i in range(len(avg_rating_by_price_range))]
    plt.bar(avg_rating_by_price_range['Price range'], avg_rating_by_price_range['Average rating'], color=colors)
    plt.xlabel('Price Range')
    plt.ylabel('Average Rating')
    plt.title('Average Rating by Price Range')
    plt.show()

def main():
    # Load Dataset
    filepath = "E:\\Internship Task\\Data Science Internship\\Dataset.csv"
    data = load_dataset(filepath)
    if data is None:
        return

    # Determine the most common price range
    most_common_price_range(data)

    # Calculate the average rating by price range
    avg_rating_by_price_range = calculate_avg_rating_by_price_range(data)

    # Visualize the average rating by price range
    visualize_avg_rating_by_price_range(avg_rating_by_price_range)

if __name__ == "__main__":
    main()
