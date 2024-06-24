#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
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

# Function to display basic statistical measures
def display_basic_statistics(data):
    numeric_columns = data.select_dtypes(include=[np.number])
    summary_stats = numeric_columns.describe()
    logging.info("Basic statistical measures for numerical columns:\n" + str(summary_stats))
    return summary_stats

# Function to calculate standard deviation
def calculate_std_deviation(data):
    numeric_columns = data.select_dtypes(include=[np.number])
    sds = numeric_columns.std()
    logging.info("Standard deviation for numerical columns:\n" + str(sds))
    return sds

# Function to visualize categorical variable distribution
def visualize_categorical_distribution(data, column):
    plt.figure(figsize=(12, 7))
    sns.set(style="whitegrid")
    sns.countplot(data=data, x=column, palette='coolwarm')
    plt.title(f"Distribution of Restaurants by {column}")
    plt.xlabel(column)
    plt.ylabel("Number of Restaurants")
    plt.xticks(rotation=45)
    plt.show()

# Function to visualize top N items in a column
def visualize_top_n(data, column, n=10):
    top_n_items = data[column].value_counts().nlargest(n).index
    data_top_n = data[data[column].isin(top_n_items)]
    
    plt.figure(figsize=(12, 7))
    sns.set(style="whitegrid")
    sns.countplot(data=data_top_n, y=column, order=top_n_items, palette='coolwarm')
    plt.title(f"Top {n} {column} with Highest Number of Restaurants")
    plt.xlabel("Number of Restaurants")
    plt.ylabel(column)
    plt.show()

    return data_top_n

# Function to display top N items and their counts in a column
def display_top_n_counts(data, column, n=10):
    top_n_counts = data[column].value_counts().nlargest(n)
    top_n_df = pd.DataFrame({column: top_n_counts.index, 'Count': top_n_counts.values})
    logging.info(f"Top {n} {column} with the Highest Number of Restaurants:\n" + str(top_n_df))
    return top_n_df

def main():
    # Load Dataset
    filepath = "E:\\Internship Task\\Data Science Internship\\Dataset.csv"
    data = load_dataset(filepath)
    if data is None:
        return

    # Display basic statistical measures
    display_basic_statistics(data)

    # Calculate standard deviation
    calculate_std_deviation(data)

    # Visualize distribution of categorical variable 'Country Code'
    visualize_categorical_distribution(data, 'Country Code')

    # Visualize top 10 cities
    top_10_cities_data = visualize_top_n(data, 'City', n=10)

    # Display top 10 cuisines
    display_top_n_counts(data, 'Cuisines', n=10)

if __name__ == "__main__":
    main()
