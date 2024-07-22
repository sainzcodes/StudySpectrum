Creating own modules

Let's create a simple program that uses some modularity. You are given three files:

1. string_utils.py (note singular "string")

2. strings_utils.py (note plural "strings")

3. main_program.py

Your task is to fill all three files with some code according to the requirements:

1. string_utils.py: this file should contain a function named halve_string that accepts a single argument: input_string. Given a string, the function should return a tuple with two string elements: the first element should contain the first half of the string, the second element should contain the second half of the string. For strings with an odd count of characters, the first element should also contain the middle character.

Example 1: halve_string('Mark') should return ('Ma', 'rk')

Example 2: halve_string('Lydia') should return ('Lyd', 'ia')

2. strings_utils.py: this file should import string_utils as a module and then use the function from point (1) to create its own function named halve_strings that accepts a single argument: a list of strings string_list. Given a list of strings, the function should return a list of tuples with halved strings, just like we explained in point (1).

Example: halve_strings(['Mark', 'Lydia']) should return [('Ma', 'rk'), ('Lyd', 'ia')]

3. main_program.py: this file should import strings_utils as a module, use the function from point (2) on the list provided in the editor (quotes), and print the return value of the function.
