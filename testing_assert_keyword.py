#here, I'll be testing how to use the assert keyword
age = 0

def enter_age age:
    age = int(input('Enter your age'))
    assert age > 0, 'Error: Invalid age entered.'
enter_age(10) # valid
enter_age(-10) #invalid

#this may be simpler to do with a while loop and if, else
#ie, finished = False
#while (finished==False):
 #   age = int(input('Enter your age.'))
  #  if (age > 0):
   #     finished = True
    #else:
     #   print ('Error: Invalid age, please try again')