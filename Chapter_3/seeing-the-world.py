travel_destinations = ['dubai','africa','london', 'washington','prince edward island']

print('\t\n Original list')
print(travel_destinations)

#sorted()temporarily puts a list in alphabetical order to maintain access to the original list

print('\t\n Temp Alph list')
print(sorted(travel_destinations))

print('\t\n Original list')
print(travel_destinations)

#Reverse alphabetical order temp and permanent syntax is different

print('\t\n Temp Reverse Alph list')
print(sorted(travel_destinations, reverse=True))

print('\t\n Original list')
print(travel_destinations)


#random reverse order

print('\t\n Non Alph Reverse')
travel_destinations.reverse()
print(travel_destinations)

print('\t\nReverse back to original')
travel_destinations.reverse()
print(travel_destinations)

#permanent alphabetical order

print('\t\nAlpha Order')
travel_destinations.sort()
print(travel_destinations)

print('\t\nAlpha Order')
travel_destinations.sort(reverse=True)
print(travel_destinations)






#Experimenting with the title Method to make all destinations in the list title case


destinations = ['dubai','africa','london', 'washington','prince edward island']

print('\t\n Original list')
print(destinations)

#sorted()temporarily puts a list in alphabetical order to maintain access to the original list

print('\t\n Temp Alph list')
print(sorted([destination.title() for destination in destinations]))

print('\t\n Original list')
print(destinations)

#Reverse alphabetical order temp and permanent syntax is different

print('\t\n Temp Reverse Alph list')
print(sorted([destination.title() for destination in destinations], reverse=True))

print('\t\n Original list')
print(destinations)


#random reverse order

print('\t\n Non Alph Reverse')
destinations.reverse()
print(destinations)

print('\t\nReverse back to original')
destinations.reverse()
print(destinations)

#permanent alphabetical order

print('\t\nAlpha Order')
destinations = [destination.title() for destination in destinations] 
destinations.sort()
print(destinations)

print('\t\nAlpha Order')
destinations = [destination.title() for destination in destinations] 
destinations.sort(reverse=True)
print(destinations)