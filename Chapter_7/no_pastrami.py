
# make sure the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwhich_orders = ['bologna','turkey','pastrami', 'pastrami', 'ham','fish', 'pastrami']
print(sandwhich_orders)
# Verify each sandwhich order until there are no more sandwhich orders.
# Move each sandwhich oder into the list of sandwhiches finished.
while 'pastrami' in sandwhich_orders:
  sandwhich_orders.remove('pastrami')
  
print(sandwhich_orders)
message = 'Sorry no pastrani available'
print(message)

   
