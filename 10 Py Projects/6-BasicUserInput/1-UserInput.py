def weather_condition(temprature):
    if temprature > 7:
        return 'Warm'
    else:
        return 'Cold'

while True:
    user_input = input('Enter temprature: ')
    if user_input == 'exit':
        break

    temprature = int(user_input)
    print(weather_condition(temprature))
