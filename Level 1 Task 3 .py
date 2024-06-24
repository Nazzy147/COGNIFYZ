#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from scipy.stats import pearsonr
import plotly.express as px
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

# Function to visualize restaurant locations on a map
def visualize_locations_on_map(data, save_path="restaurant_locations.html"):
    world_map = folium.Map(location=[0, 0], zoom_start=2)
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=2,
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(world_map)
    world_map.save(save_path)
    logging.info(f"Map saved to {save_path}")

# Function to visualize distribution of restaurants across top N cities
def visualize_distribution_across_cities(data, n=10):
    top_n_cities = data['City'].value_counts().nlargest(n).index
    data_top_n_cities = data[data['City'].isin(top_n_cities)]
    
    plt.figure(figsize=(12, 7))
    sns.set(style="whitegrid")
    sns.countplot(data=data_top_n_cities, y='City', order=top_n_cities, palette='coolwarm')
    plt.title(f"Distribution of Restaurants Across Top {n} Cities")
    plt.xlabel("Number of Restaurants")
    plt.ylabel("Name of Cities")
    plt.show()

    return data_top_n_cities

# Function to visualize correlation between restaurant location and rating
def visualize_correlation(data):
    correlation_matrix = data[['Latitude', 'Longitude', 'Aggregate rating']].corr()
    
    plt.figure(figsize=(10, 8))
    sns.set(style="whitegrid")
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title("Correlation Between Restaurant's Location and Rating")
    plt.show()

def main():
    # Load Dataset
    filepath = 'E:\\Internship Task\\Data Science Internship\\Dataset.csv'
    data = load_dataset(filepath)
    if data is None:
        return

    # Visualize restaurant locations on a map
    visualize_locations_on_map(data)

    # Visualize distribution of restaurants across top 10 cities
    visualize_distribution_across_cities(data, n=10)

    # Visualize correlation between restaurant location and rating
    visualize_correlation(data)

if __name__ == "__main__":
    main()
