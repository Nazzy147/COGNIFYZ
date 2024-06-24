#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

# Function to display dataset info
def display_dataset_info(data):
    logging.info("Displaying dataset information...")
    print(data.info())

# Function to check for duplicates
def check_duplicates(data):
    dup_count = data.duplicated().sum()
    logging.info(f"Number of duplicate rows: {dup_count}")
    return dup_count

# Function to check for missing and empty values
def check_missing_empty_values(data):
    missing_values = data.isna().sum()
    empty_values = (data == "").sum()
    logging.info("Missing values count per column:")
    logging.info(f"\n{missing_values}")
    logging.info("Empty values count per column:")
    logging.info(f"\n{empty_values}")
    return missing_values, empty_values

# Function to clean data
def clean_data(data, column):
    data = data[data[column] != ""]
    logging.info(f"Rows with empty values in '{column}' column removed.")
    return data

# Function to visualize target variable distribution
def visualize_distribution(data, column):
    plt.figure(figsize=(12, 7))
    sns.set(style="whitegrid")
    sns.countplot(x=column, data=data, palette='coolwarm')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

# Function to check balance in distribution
def check_balance(data, column):
    target_counts = data[column].value_counts()
    is_balanced = np.all(target_counts >= target_counts.mean())
    balance_status = "balanced" if is_balanced else "not balanced"
    logging.info(f"The distribution of the target variable is {balance_status}.")

def main():
    # Load Dataset
    filepath = "E:\\Internship Task\\Data Science Internship\\Dataset.csv"
    data = load_dataset(filepath)
    if data is None:
        return

    # Display top rows of the dataset
    logging.info("Top 10 rows of the dataset:")
    logging.info(f"\n{data.head(10)}")

    # Check number of rows and columns
    logging.info(f"Number of rows: {data.shape[0]}")
    logging.info(f"Number of columns: {data.shape[1]}")

    # Check for duplicates
    check_duplicates(data)

    # Check for missing and empty values
    check_missing_empty_values(data)

    # Remove rows with empty values in the 'Cuisines' column
    data = clean_data(data, 'Cuisines')

    # Verify no empty values after cleaning
    _, empty_values_after_removal = check_missing_empty_values(data)
    logging.info(f"Empty values count after removal: {empty_values_after_removal.sum()}")

    # Display basic information about the dataset
    display_dataset_info(data)

    # Visualize distribution of the target variable
    visualize_distribution(data, 'Aggregate rating')

    # Check if the distribution is balanced
    check_balance(data, 'Aggregate rating')

if __name__ == "__main__":
    main()
