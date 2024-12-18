#loops up until the number before the second number in the range
for value in range(1,21):
   print(value)
    
#for value in list(range(1,1000001)):
 # print(value)
    
    
numbers= list(range(1,1000001))
 
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#looping through the odds
for value in range(3,20,2):
    print(value)
    
#multiples of 3 two ways of doing it

multiples = []

for value in range(3,30):
    multiple = value*3
    multiples.append(multiple)

print(multiples)
    

multiples= [value*3 for value in range(3,30)]

for multiple in multiples:
    print(multiple)
    
    
#cubes

cubes= [value**3 for value in range(1,10)]

for cube in cubes:
    print(cube)
    
#list comprehension

cubes= [value**3 for value in range(1,10)]
print(cubes)