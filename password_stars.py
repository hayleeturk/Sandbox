MINIMUM = 10
password_attempt = input("Enter password: ")
while len(password_attempt) < MINIMUM:
    print("Password must be at least 10 characters")
    password_attempt = input("Enter password: ")
if len(password_attempt) >= MINIMUM:
    print("Great password!")

