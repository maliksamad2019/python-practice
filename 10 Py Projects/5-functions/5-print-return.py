def mean(myList):
    print('Function started')
    the_mean = sum(myList)/len(myList)
    # print(the_mean)
    # return None # by default return is None
    return the_mean

mymean = mean([10,23,63,43])
# print(mymean + 10)) # None +10 will give error
print(mymean)
