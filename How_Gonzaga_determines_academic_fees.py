#in this program, I will determine a student's characteristics, as well as if he recieves a discount on fees
# this is my first time creating a class in python too

class Determining_Academic_Fees:
    def __init__(self, firstname, lastname, year, plays_rugby):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.playsrugby = plays_rugby
        
    def determine_fees(self):
        fees = 7400 #actual fees for Gonzaga for 2022/23
        if (self.year<1 or self.year>6):
            fees = 0
        elif (self.playsrugby=='True'):
            fees /= 2
        elif (self.playsrugby=='False'):
            fees = 7400
    
        
        if (fees==0):
            print ('The fees for 2022/23 for %s %s are €%d, as he\'s not attending the school.' % (self.firstname, self.lastname, fees))
        elif (fees==(7400/2)):
            print ('The fees for 2022/23 for %s %s are €%d, as we feel that %s is the personification of our ethos.' % (self.firstname, self.lastname, fees, self.firstname))
        else:
            print ('The fees for 2022/23 for %s %s are €%d.' % (self.firstname, self.lastname, fees))    
        return 3


print ('Please enter your the following:')
first_name = input('First name:\n>')
last_name = input('Last name:\n>')
academic_year = int(input('Current year (if graduated, enter 7):\n>'))
plays_Rugby = (input('Do you play rugby (True or False):\n>'))

user = Determining_Academic_Fees(first_name, last_name, academic_year, plays_Rugby)

user.determine_fees()

# python determine_academic_fees.py