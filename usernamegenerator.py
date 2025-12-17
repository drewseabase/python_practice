first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
username = first_name[:3] + last_name[:3]
print(f'Your username is {username}')