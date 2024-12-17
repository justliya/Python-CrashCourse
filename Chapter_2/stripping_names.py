#Stripping white and using tabs and newlines for cleaner organized code 
name = "    Jack Johnson     "

print("\n\tOriginal:\n" + name)

print("\n\tLeft White Space Gone:\n" + name.lstrip())

print("\n\tRight White Space Gone:\n" +name.rstrip())

print("\n\tAll White Space Gone:\n" +name.strip())