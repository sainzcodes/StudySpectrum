import string_utils

def halve_strings(string_list): # Define the function to apply halve_string to each string in a list

    to_return = [] # Initialize an empty list to store the results
    for string in string_list: # Loop through each string in the provided list
        to_return.append(string_utils.halve_string(string)) # Append the result of halving the string to the list
    return to_return # Return the list of tuples, each containing two halves of the original strings
