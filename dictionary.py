'''
Use CSV module to read the Parking.csv and use nested dictionaries to store each parking ticket as a single dictionary 
into a large list of dictionaries named tickets.
'''
import csv 

# Create list variable 'tickets' that stores dictionaries 
tickets = []
# Open CSV file, use for loop to read through CSV file, and create a dictionary associated
# with values in each row 
with open('Parking.csv') as parking_csv:
    reader = csv.DictReader(parking_csv)
    for row in reader:   
        d = dict(row)
        tickets.append(d)
#test 
print(tickets)
