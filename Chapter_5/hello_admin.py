#using if else to loop through a list and print customized greetings
#including an if statement message just in case the list is empty before looping through list to prevent a blank output

usernames =['admin', 'justliya', 'catgirl', 'word_woman', 'believe-up']

if usernames == []:
    print('We need to find users')
          
for name in usernames:
    if name == 'admin':
        print('Hello ' + name + ', would you like a status report?')
    else:
        print('Hello '+ name + ', thank you for logging in again.')
        
