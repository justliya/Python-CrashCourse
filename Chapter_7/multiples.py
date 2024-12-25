# Convert the input to an integer then when including the response in an if else elif statement convert it back to a string

multiple = int(input("Pick any number?"))

if multiple % 10 == 0:
    print(str(multiple)+ ", is a multiple of 10")
else:
    print(str(multiple) + ", is not a multiple 10")