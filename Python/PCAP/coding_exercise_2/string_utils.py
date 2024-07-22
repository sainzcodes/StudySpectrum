import math

def halve_string(input_string): # Define the function to split a string into two halves
    middle = math.ceil(len(input_string) / 2) # Calculate the middle index of the string, rounding up for odd lengths
    return (input_string[:middle], input_string[middle:]) # Return a tuple containing the first half and the second half of the string
