
# args will be a tuples
def means(*args):
    num_args = [num for num in args if isinstance(num, int) or isinstance(num,float)]
    # print(num_args)
    return sum(num_args)/len(num_args)

print(means(1,2,3,4,'34',4.3))

# kwargs will be a dictionary 
def means_keyword_args(**kwargs):
    return kwargs

print(means_keyword_args(a=1,b=2,c=3,d=4))
