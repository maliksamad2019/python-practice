monday_temperatures = [9.1,8.8,7.5]
print(monday_temperatures)

# add 1 element at the end
monday_temperatures.append(8.1)
print(monday_temperatures)

# remove all elemtents
monday_temperatures.clear()
print(monday_temperatures)

monday_temperatures = [9.1,8.8,7.5]
# will print index of that element
print(monday_temperatures.index(8.8))

# will give error if it is not in list
print(monday_temperatures.index(8.8,2))
# print(monday_temperatures.index(8.1))


