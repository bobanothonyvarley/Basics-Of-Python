#here, I'm going to explain how the keyword 'yield' in python works

#yield is very similiar to return, except will only return 1 value everytime, ie,

def return_function():
    number = 1
    return number
    #I could write more code below the return statement, but it'd be a waste of time, as it will never be reached, no matter how many times I reference return_function()
    
#now, to create a yield function


def yield_function():
    number = 1
    yield number   #yield_list = 1
    number = 2
    yield number   #yield_list = [1, 2]
    number = 3
    yield number   #yield_list = [1, 2, 3]
    
#here, after the first time it's called, it will start at the beginning and execute all the way down to the first yield, and return number
#after the second time it's called, it will start after the first yield, and execute all the way down to the second yield, and return number
#after the third time it's called, it will start after the second yield, and execute all the way down to the third yield, and return number


returned_value = return_function()
print (returned_value)

yield_list = yield_function()

for number in yield_list:
    print (number)

#python explaining_yield_keyword.py
