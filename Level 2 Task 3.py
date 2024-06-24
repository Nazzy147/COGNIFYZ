#!/usr/bin/env python
# coding: utf-8

import pandas as pd
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

# Function to extract additional features
def extract_additional_features(data):
    data['Restaurant Name Length'] = data['Restaurant Name'].apply(len)
    data['Address Length'] = data['Address'].apply(len)
    logging.info("Extracted additional features: 'Restaurant Name Length' and 'Address Length'")
    return data

# Function to encode categorical variables
def encode_categorical_variables(data):
    data['Has Table Booking'] = data['Has Table booking'].apply(lambda x: 1 if x == "Yes" else 0)
    data['Has Online Delivery'] = data['Has Online delivery'].apply(lambda x: 1 if x == "Yes" else 0)
    logging.info("Encoded categorical variables: 'Has Table Booking' and 'Has Online Delivery'")
    return data

def main():
    # Load Dataset
    filepath = "E:\\Internship Task\\Data Science Internship\\Dataset.csv"
    data = load_dataset(filepath)
    if data is None:
        return

    # Extract additional features
    data = extract_additional_features(data)

    # Display the updated DataFrame
    logging.info("Top 5 rows of the dataset with additional features:\n" + str(data.head()))

    # Encode categorical variables
    data = encode_categorical_variables(data)

    # Display the updated DataFrame
    logging.info("Top 5 rows of the dataset with encoded variables:\n" + str(data.head()))

if __name__ == "__main__":
    main()
