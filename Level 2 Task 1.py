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

# Function to calculate percentage of restaurants offering table booking and online delivery
def calculate_percentages(data):
    total_num_restaurants = len(data)
    table_booking_percentage = (data['Has Table booking'] == 'Yes').sum() / total_num_restaurants * 100
    online_delivery_percentage = (data['Has Online delivery'] == 'Yes').sum() / total_num_restaurants * 100
    logging.info(f"Percentage of restaurants that offer Table Booking: {table_booking_percentage:.2f}%")
    logging.info(f"Percentage of restaurants that offer Online Delivery: {online_delivery_percentage:.2f}%")
    return table_booking_percentage, online_delivery_percentage

# Function to compare average ratings of restaurants with and without table booking
def compare_average_ratings(data):
    avg_rating_with_table = data[data['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
    avg_rating_without_table = data[data['Has Table booking'] == 'No']['Aggregate rating'].mean()
    logging.info(f"Average rating with Table Booking: {avg_rating_with_table:.2f}")
    logging.info(f"Average rating without Table Booking: {avg_rating_without_table:.2f}")
    return avg_rating_with_table, avg_rating_without_table

# Function to analyze online delivery availability by price range
def analyze_online_delivery_by_price_range(data):
    data['price_ranges'] = pd.cut(data['Average Cost for two'],
                                  bins=[0, 500, 1000, float('inf')],
                                  labels=['Low', 'Medium', 'High'])
    online_delivery_by_price_range = pd.crosstab(data['price_ranges'], data['Has Online delivery'], normalize='index')
    logging.info("Online Delivery Availability by Price Range:\n" + str(online_delivery_by_price_range))
    return online_delivery_by_price_range

# Function to visualize online delivery availability by price range
def visualize_online_delivery_by_price_range(data):
    plt.figure(figsize=(12, 7))
    sns.set(style="whitegrid")
    sns.countplot(data=data, x='price_ranges', hue='Has Online delivery', palette='coolwarm')
    plt.title('Online Delivery Availability by Price Range')
    plt.xlabel('Price Range')
    plt.ylabel('Count')
    plt.show()

def main():
    # Load Dataset
    filepath = "E:\\Internship Task\\Data Science Internship\\Dataset.csv"
    data = load_dataset(filepath)
    if data is None:
        return

    # View top 10 rows of the dataset
    logging.info("Top 10 rows of the dataset:\n" + str(data.head(10)))

    # Calculate percentage of restaurants offering table booking and online delivery
    calculate_percentages(data)

    # Compare average ratings of restaurants with and without table booking
    compare_average_ratings(data)

    # Analyze online delivery availability by price range
    analyze_online_delivery_by_price_range(data)

    # Visualize online delivery availability by price range
    visualize_online_delivery_by_price_range(data)

if __name__ == "__main__":
    main()
