# WeatherExplorer

## Overview
WeatherExplorer is a Python project that explores weather data for various cities. It retrieves weather information using the OpenWeatherMap API, analyzes the data, and visualizes the relationships between weather variables and geographic coordinates. Additionally, the project incorporates the Geoapify API to find hotels near cities that meet specific weather conditions.

# About
Using two API's Weather API, and Geoapify API.  I pull random city data points from all over the globe and analze these points based on different criteria (Temperature, cloudiness, humidity, wind speed) and how they compare between the two hemispheres.  The second part of this project, was taking the data points, filtering them based on what I think would be nice vacation weather.  Then using Geoapify API look for the closest hotels near these cities.  Maybe I will find my next vacation destination?

# Features
* __Data Retrieval:__ Utilizes the OpenWeatherMap API to fetch weather data for cities based on geographic coordinates.
* __Visualization:__ Generates scatter plots to showcase relationships between latitude and weather variables (temperature, humidity, cloudiness, wind speed).
* __Hotel Search:__ Uses the Geoapify API to find hotels near cities that meet ideal weather conditions.
* __Interactive Maps:__ Utilizes Hvplot to create interactive maps, visualizing city data and displaying hotel information in hover tooltips.
  
# How to Use
1) __Generate City Data:__ Run the `WeatherPy` script to generate a list of cities and fetch weather data.
2) __Visualize Data:__ Explore the relationships between latitude and weather variables using scatter plots generated by the script.
3) __Find Ideal Cities:__ Use the generated data to identify cities with ideal weather conditions based on specific criteria.
4) __Discover Nearby Hotels:__ The script uses the Geoapify API to find hotels near selected cities and displays the information on an interactive map.

# Requirements
* Python 3.x
* Required Python packages (specified in the requirements.txt file)
* OpenWeatherMap API key (place it in api_keys.py)
* Geoapify API key (place it in api_keys.py)

# Installation
1) Clone the repository:
```bash
git clone https://github.com/yourusername/WeatherExplorer.git
```
2) Install required packages:
```bash
pip install Hvplot, pandas, Requests, Matplotlib
```
3) Place your API keys in the `api_keys.py` file.

# Usage
1) Run the `WeatherPy` script:
```bash
python WeatherPy.py
```
2) Explore the generated scatter plots and identify cities with ideal weather conditions.
3) Run the `VacationPy` script to find hotels near selected cities and visualize the data on an interactive map:
```bash
python VacationPy.py
```
# Acknowledgments
* OpenWeatherMap API
* Geoapify API
* Hvplot
* Pandas
* Requests
* Matplotlib

![image](<output_data/Fig1.png>)

![image](<output_data/Fig2.png>)

![image](<output_data/Fig3.png>)

![image](<output_data/Fig4.png>)

linearregression.py:
This function utilizes five inputs, two of these are different data sets that need to be compared (x, y).  Three other inputs that will label the x_axis, y_axis, and the title of the plot.  Once the functions five inputs are satisfied it will compute the linear regression line utilizing scipy linregress function and matplotlib.pyplot for plotting both the scatter graph and the linear regression line.

# Contributing
Erika Walker

