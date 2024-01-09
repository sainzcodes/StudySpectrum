'''All Roads Lead to Rome

You are given a list with various flight connections in Europe. Each connection is represented as a tuple with the following elements:

(city_from, city_to, time)

For example, the following tuple represents a flight from Amsterdam to Dublin which takes 100 minutes:

('Amsterdam', 'Dublin', 100)

Your task is to go through all the routes in a loop and check how many of them lead to Rome (i.e. how many of them have city_to equal to 'Rome'). Among the routes to Rome, you should also calculate the average flight time. Print the following the output:

{} connections lead to Rome with an average flight time of {} minutes

Replace {} with the number of connections and the average flight time. '''

# List of the given connections
'''
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

# Initializing variables to keep track of data
total_flight_time = 0
connections_to_rome = 0

# Iteration trough the 'connection' lists using a loop'
for connection in connections:
    city_from, city_to, time = connection

    #Check if the destination is Rome
    if city_to == 'Rome':
        total_flight_time += time 
        connections_to_rome += 1

# Check if there are connections to Rome
if connections_to_rome > 0:
    average_flight_time = total_flight_time / connections_to_rome
    print("{} connections lead to Rome with an average flight time of {} minutes".format(connections_to_rome, average_flight_time))
else:
    print("No connections lead to Rome.")'''

# Solution provided by the book:
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170)
    ]
     
counter = 0
sum = 0.0
     
for con in connections:
    if con[1] == 'Rome':
        counter += 1
        sum += con[2]
     
print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')



