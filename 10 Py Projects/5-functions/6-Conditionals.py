def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) /len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

student_grades = {'malik':9.1, 'samad':8.8, 'john': 7.5}
monday_temperatures = [8.8,9.1,9.9]
print(mean(student_grades))
print(mean(monday_temperatures))
   
print( isinstance(student_grades,list))
print( isinstance(student_grades,dict))
print( isinstance(monday_temperatures,list))
print( isinstance(monday_temperatures,dict))


x = 4
y = 1

if x > y:
    print('x is greater then y')
else:
    print('x is less then y')