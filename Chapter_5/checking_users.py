#looping through two list of  usernames and sending a message to new users if username is already taken

current_users = ['updawg', 'justliya', 'Catgirl', 'word_woman', 'believe-up']
new_users = ['updawg', 'Justliya', 'candygirl', 'Mer-Maid', 'twenty']

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for name in new_users:
    # Check case-insensitively by converting name to lowercase
    if name.lower() in current_users_lower:
        print("Username " + name + " is already taken.")
    else:
        print("Welcome aboard " + name + ", you have successfully created an account!")
        current_users.append(name)  # Add new user to current_users
        current_users_lower.append(name.lower())  # Update the lowercase list

# The results
print("\nUpdated current users:")
print(current_users)