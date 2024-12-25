# for while True loop you have to make sure you define the variables outside of while True first


# Use a break statement to exit the loop when the user enters a 'quit' value.

toppings = "What toppings would you like on your pizza?"
toppings += "\n(if you would like to exit type 'quit')"


while True:   
    pizza = input(toppings)
    
    if pizza == 'quit':
        print("Thank you, goodbye")
        break
    else:
        print( pizza + ', has been added')
        
        
        
# conditional test in the while statement to stop the loop.

toppings = "What toppings would you like on your pizza?"
toppings += "\n(if you would like to exit type 'quit')"

pizza = ""

while pizza != 'quit':
     pizza = input(toppings)
     
     if pizza != 'quit':
         print( pizza + ', has been added')
         
        
# active variable to control how long the loop runs. can be used in games to make ending less complicated by only checking one condition (Flag)

toppings = "What toppings would you like on your pizza?"
toppings += "\n(if you would like to exit type 'quit')"

active = True
while active:
   message = input(toppings)
  
   if message == 'quit':
    active = False
   else:
    print(message)
