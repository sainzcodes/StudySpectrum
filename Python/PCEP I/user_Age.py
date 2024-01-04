user_age = int(input('What is your age? '))
user_country = int(input('What is your Country of origin? '))

if user_age < 25 and user_country == 'Germany' or user_country == 'Denmark' or user_country == 'Norway':
	print('You can apply for a German student exchange programme')
else: 
	print('Sorry you do not qualify')