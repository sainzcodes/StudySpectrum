# Within 10 days from the day of purchase, given that you have not used the item, or
# No matter when you bought it, when the item broke down through no fault of your own.

purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = str(input('Have you used the item at all [y/n]? '))
is_broken = str(input('Has the item broken down on its own [y/n]? '))

if purchase_date < 10 and is_used == 'n' or is_broken == 'y':
	print('You can get a refund.')
else:
	print('You cannot get a refund.')