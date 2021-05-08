user_input = input('Enter your name: ')
age = int(input('Enter your Age: '))

message = "Hello %s! are you %s?" % (user_input , age)
print(message)

message = f"Hello {user_input}! are you {age}?"
print(message)
