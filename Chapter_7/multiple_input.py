# Moving Items from One List to Another

# Start with sandwhiches that need to be made,
# and an empty list to hold made sandwhiches

sandwhich_orders = ['bologna','turkey', 'ham','fish']
finished_sandwhich = []

# Verify each sandwhich order until there are no more sandwhich orders.
# Move each sandwhich oder into the list of sandwhiches finished.
while sandwhich_orders:
  current_order = sandwhich_orders.pop()
 
  print("Verifying order: " + current_order.title())
  finished_sandwhich.append(current_order)

# Display all finished sandwhiches.

print("\nThe following sandwhiches has been made:")
for finished_order in finished_sandwhich:
   print(finished_order.title())
   
