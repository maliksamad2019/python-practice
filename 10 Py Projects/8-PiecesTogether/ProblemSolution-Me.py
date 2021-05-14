
text = ''

while True:
    user_input = input('Say somthing: ').capitalize()
    if user_input == '\\end':
        break
    text = f"{text}{user_input}. "

print(text)



