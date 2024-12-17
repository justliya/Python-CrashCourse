#Dinner Guest List personal invite message using list index id to print a personal message to each name stored in the list

invitees = ['Jaxon', 'Ben', 'Zay', 'Alison']

print("\n\tDinner Guest List")

print('\n' + str(invitees))

print('\nHi ' + invitees[-1] + ', I would like to invite you to a special dinner!')

print('\nHi ' + invitees[-2] + ', I would like to invite you to a special dinner!')

print('\nHi ' + invitees[-3] + ', I would like to invite you to a special dinner!')

#Modifying guest list

print('\n' + invitees[-2] + ", can't make it this time.")

invitees[-2] = 'Layla'

print('\nHi ' + invitees[-1] + ', I would like to invite you to a special dinner!')

#inserting new guest 

print("\n\tNew Guest")

#beginning 
invitees.insert(0, 'Clifford')

print('\nHi ' + invitees[0] + ', I would like to invite you to a special dinner!')

#middle
invitees.insert(3, 'Alex')

print('\nHi ' + invitees[3] + ', I would like to invite you to a special dinner!')

#end
invitees.insert(-1, 'Sarah')

print('\nHi ' + invitees[-1] + ', I would like to invite you to a special dinner!')

print('\n' + str(invitees))


print("\n\tNow there is only space for two people at the dinner shoot!")

#now using the popped method to remove guest at the end of the list not completing deleting the value because we still have access to it in a new variable

removed_guest = invitees.pop()

print('\n So sorry ' + removed_guest + ' there is no longer spaces at the table I will get you next time!')

removed_guest = invitees.pop()

print('\n So sorry ' + removed_guest + ' there is no longer spaces at the table I will get you next time!')

removed_guest = invitees.pop()

print('\n So sorry ' + removed_guest + ' there is no longer spaces at the table I will get you next time!')

removed_guest = invitees.pop()

print('\n So sorry ' + removed_guest + ' there is no longer spaces at the table I will get you next time!')
removed_guest = invitees.pop()

print('\n So sorry ' + removed_guest + ' there is no longer spaces at the table I will get you next time!')

#commas are needed after list index in order to concatenate a string with proper syntax

print('\n\t'+ invitees[0] , 'and' , invitees[1] + ' are the remaining guest at the table')

