"""
Set of functions to create a classifier of Fahrenheit temperatures
"""

def fahr_to_celsius(temp_fahrenheit):
    """Converts Fahrenheit degrees to Celsius degrees
    
    Accepted parameters:
    temp_fahrenheit <float>: Temperature in Fahrenheit degrees
    
    Returns:
    Temperature in Celsius degrees
    
    """
    #Convert the input using the provided formula
    converted_temp = (temp_fahrenheit - 32) / 1.8
    #Return the value contained in the converted_temp variable
    return converted_temp


def temp_classifier(temp_celsius):
    """
    Classifies temperatures in Celsius degrees as follows:
    Below -2°C == 0
    Equal or above -2°C and below 2°C == 1
    Equal or above 2°C and below 15°C == 2
    Equal or above 15°C == 3
    
    Parameters accepted:
    temp_celsius <float>: Temperature in Celsius degrees.
    
    Returns:
    A reclassified value from 0 to 3   
    
    """
    value = None
    if temp_celsius < -2:
        value = 0
    elif temp_celsius < 2:
        value = 1
    elif temp_celsius < 15:
        value = 2
    else:
        value = 3
    return value