#experimenting with exit()

from sys import exit

amount_taken = int(input("""Congradulations, you have just stumbled upon a room
filled to the brim with narcotics, how many grams shall you take?\n>"""))

if amount_taken==0:
    print ('Ah, a good, upstanding citizen!')
    exit(0)
elif amount_taken<13:
    print ('For recreational purposes, I see.')
else:
    print ('You clearly have an entrepreneurial spirit!')

hiding_place = input('Where do you intend to hide these substances?\n>')
print ('Thanks, I\'ll make a hefty amount of money reporting you to the authorities, lol')
