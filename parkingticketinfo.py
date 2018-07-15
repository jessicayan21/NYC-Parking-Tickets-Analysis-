# Find the number of open violations and the total dollar amount due of all open violations
# for the corresponding plate 

def amount_owed(tickets, plate):
    # Initialize variables 
    match = []
    amount_due = []
    total = 0
    result_tuple = ()
    
    # Find the number of times the plate value appears in 'tickets' 
    # use for loop to iterate through 'tickets'and check if value matches plate
    for i in tickets:
        correct = i['Plate']
        
        # If the value of the variable 'repeat' matches the plate parameter, 
        # append to the 'match' list, create variable 'amount' that contains value 
        # of 'Amount Due', and append the amount to list 'amount_due'. These lists will 
        # be used to find the number of violations and the total amount due for a plate 
        if correct == str(plate):
            amount = i['Amount Due']
            match.append(correct)
            amount_due.append(amount)

    # Strips '$' in all the amounts in the list 'amount_due' so that the strings can be 
    # converted to floats and be added together 
    for amount in amount_due:
        num = float(amount.lstrip("$")) 
        total += num

    # Find the length of the 'match' list to determine the plate's number of violations
    count = len(match)
    
    # Store and return a tuple that contains both the number of open violations and 
    # the total dollar amount due for all open violations
    result_tuple = (count, total)
    return result_tuple

# Call function
amount_owed(tickets, "NAX52C")
