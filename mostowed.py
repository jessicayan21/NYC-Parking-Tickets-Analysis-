# Find plate number and associated total amount due for the diplomatic car that owes the most money over time 

def most_owed(tickets):
    # Initialize variables to be used later 
    plate = row['Plate']
    all = []
    d_plates = {}
    num_max = 0
    result_tuple = () 
    
    # Using a for loop, call function amount_owed to find out how much each car owes 
    # and combine into a dictionary of plates (keys) associated with tuples (values)
    # of the number of open violations and the total dollar amount due for all 
    # open violations
    for i in tickets:
        plate = i['Plate']
        all = amount_owed(tickets, plate) 
        d_plates[plate] = all
    
    # FIND MAX AMOUNT DUE:
    # Use for loop to iterate through 'd_plates' and create a variable 'current' that 
    # stores the value of the amount owed for each car.
    # Compare the 'current' value with 'num-max' to find the maximum - if 'current'
    # is greater than 'num_max', 'num_max' will update itself to become this larger value    
    for j in d_plates:
        current = d_plates[j][1]
        if current > num_max:
            num_max = current
    
    # FIND PLATE WITH ASSOCIATED MAX AMOUNT DUE:
    # Use a for loop to find the key associated with the 'num_max' value in the dictionary
    for k in d_plates:
        if d_plates[k][1] == num_max:
            found_plate = k
            
    # Store and return a tuple, 'result_tuple', with the plate of the car and the max
    # amount owed
    result_tuple = (found_plate, num_max)
    return result_tuple

# Call function 
most_owed(tickets) 
