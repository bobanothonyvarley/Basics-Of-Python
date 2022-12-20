#testing how to use the global keyword

x = 10 #global variable

def some_function():
    global x #we need to reference it as global to access it the x = 10 above
    x += 5

some_function()

print (x, '\n') #should print 15

y = 10

def second_function():
    y = 5              #here, the program creates a local variable called y, seperate (and oblivious) to the global variable y
    print (y, '\n')    

second_function()

print (y)

#this would print out 5, then 10