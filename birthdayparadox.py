#py birthdayparadox.py

k=23
n=365

cons=1

i=1
while (i<k):
    
    cons*= ( (n-i)/n )
    i+=1
    print("the probability is ", 1-cons, "for ", i, "people")