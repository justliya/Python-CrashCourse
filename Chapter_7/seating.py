#if input is an integer make sure to convert to an integer for an if statement

table = int(input('How many people are in your party?'))

if table < 8:
    print("Your table is ready") 
else:
    print("Sorry you are going to have a bit of a wait for your party size")