# a = 3
# while a > 0:
#     print(a)
#     a-=1
username = ''

# while username != 'pypy':
#     username = input('Enter username: ')

while True:
    username = input('Enter username: ')
    if username == 'pypy':
        break
    else:
        continue

print(f"hello {username}")
