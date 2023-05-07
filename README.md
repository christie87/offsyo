# US Restaurants with Zomato Ratings Dashboard

This project builds a dashboard that allows users to explore US restaurants' Zomato ratings based on cuisine. The dashboard has three tabs:
- **Cities:** displays a sunburst chart that shows the distribution of restaurants across different cities and rating categories.
- **Restaurants:** displays a bubble chart that shows the relationship between a restaurant's aggregate rating, rating text, and number of votes.
- **Top Rated:** displays a bar chart that shows the average aggregate rating of the top-rated restaurants in each city for the selected cuisine.

## Table of Contents

- [Tech Stack](#techstack)
- [Data Source](#datasource)
- [Deployment](#deployment)
- [Usage](#usage)
- [Features](#features)


## Tech Stack

The dashboard is built using the following technologies:
- Python 3.8
- Plotly: a data visualization library that provides interactive charts and graphs.
- Dash Bootstrap Components: a library of Bootstrap components built for use with Plotly Dash.
- Pandas: a Python library for data manipulation and analysis.


## Data Source

The data used in this project comes from the Zomato Restaurants dataset, available on Kaggle [here](https://www.kaggle.com/shrutimehta/zomato-restaurants-data). The dataset contains information about restaurants from various countries worldwide, including their location, cuisine, rating, and more. The US subset of the dataset is used in this project.

## Deployment

The [dashboard](https://us-zomato-restaurants.onrender.com) is deployed on Render, a cloud platform that offers scalable and easy-to-use infrastructure for web applications, using the free tier.

## Usage

To use this app, follow these steps:

1. Select a cuisine type from the dropdown menu.
2. Explore the data using the tabs: 
    - Cities: Displays a sunburst chart of the cities where the selected cuisine is available and their corresponding Zomato ratings.
    - Restaurants: Displays a bubble chart of the restaurants serving the selected cuisine in different cities, showing their Zomato ratings and votes.
    - Highest Rated: Displays a bar chart of the top-rated restaurants ('Excellent') for the selected cuisine in different cities.
    
## Features

This app includes the following features:

- Dropdown menu for selecting a cuisine type.
- Three tabs for exploring data on cities, restaurants, and highest rated restaurants.
- Interactive graphs using the Plotly library:
    - Sunburst chart for cities.
    - Bubble chart for restaurants.
    - Bar chart for highest rated restaurants.
- Responsive layout using the Bootstrap library.



Thank you for using our US Restaurants with Zomato Ratings Dashboard app!

