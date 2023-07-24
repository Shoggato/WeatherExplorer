# World Weather API calls and Vacation Ideas

##Introduction:

Using two API's Weather API, and Geoapify API.  I pull random city data points from all over the globe and analze these points based on different criteria (Temperature, cloudiness, humidity, wind speed) and how they compare between the two hemispheres.  The second part of this project, was taking the data points, filtering them based on what I think would be nice vacation weather.  Then using Geoapify API look for the closest hotels near these cities.  Maybe I will find my next vacation destination?

Within the python-api-challenge github, you will find three folders.  Output_data, VacationPy, WeatherPy.  

    ##Output_data folder: 
    Holds any information that needs to be saved such as figures and the data cities.csv that is pulled from the internet using Weather API.  

    ##WeatherPy folder:
    Stores the Jupyter notebook file, along with two other Python files.  linearregression.py, and api_keys.py 

        ##linearregression.py:
        This function utilizes five inputs, two of these are different data sets that need to be compared (x, y).  Three other inputs that will label the x_axis, y_axis, and the title of the plot.  Once the functions five inputs are satisfied it will compute the linear regression line utilizing scipy linregress function and matplotlib.pyplot for plotting both the scatter graph and the linear regression line.

        ##api_keys.py
        This holds my API keys for both Weather API and Geoapify

    ##VactionPy:
    Holds my second part of my project VacationPy Jupyter notebook, as well as a duplicate file of api_keys.py.



