#Generates random phone number and address

import random

def generator():
	num_3 = random.randint(000, 999)

	num_4 = random.randint(0000, 9999)

	num_5 = random.randint(00000, 99999)

	streets = ['Second','Third','First', 'Fourth','Park', 'Fifth', 'Main', 'Sixth',
 			'Oak', 'Seventh', 'Pine', 'Maple', 'Cedar', 'Eighth', 'Elm', 
 			'View', 'Washington', 'Ninth', 'Lake', 'Hill']

	ran_street = random.choice(streets)

	cities = ['Chicago', 'New York', 'Washington', 'Highland', 'Lamont', 'Austin', 
			'Los Angeles', 'Detroit', 'Naperville', 'Oswego', 'Cicero']
	ran_cities = random.choice(cities)

	abr = ['st', 'ave', 'blvd', 'rd']

	ran_abr = random.choice(abr)

	states = ['AK',	'Al', 'AZ',	'AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN',
			'IA','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH']

	ran_state = random.choice(states)

	print('1-{}-{}'.format(num_3, num_4))
	print('{} {} {}'.format(num_4, ran_street, ran_abr))
	print('{} {} {}'.format(ran_cities, ran_state, num_5))

generator()
print('\n')
generator()