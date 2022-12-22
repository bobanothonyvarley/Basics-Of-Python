#here, I'm going to be experimenting with dict(ionairie)s

description = {'name': 'David Anthony Varley', 'age': 18, 'height': '6\'2'}

print (description['name'])
#must be stored in a dict as a string with ' ', ie description[name], even if it was stored as - name: - and not - 'name': - would not work
#ie, try this (It won't work):
# print (description[name])

print ('Now, let\'s just get some information about you\n') 

description['favourite_colour'] = input('What is your favourite colour?\n>') #does the user need to put ' ' around their answer? I presume not
description['sport'] = input('What\'s your favourite sport?\n>')
print ('')
print ('Here is your description:\n', description)
print ('\n\n\n'




#here, I'll experiment with dicts in a bit more detail, what functions to use with them and what to do if an element doesn't exist

#create some dictionairies
number_of_counties = {'Leinster': 12, 'Munster': 6, 'Ulster': 9, 'Connacht': 5}
cities_of_provinces = {'Leinster': 'Dublin', 'Munster': 'Cork', 'Ulster': 'Belfast', 'Connacht': 'Galway'}

#add some more detail
number_of_counties['NI'] = 6
cities_of_provinces['NI'] = 'Belfast'


#print to check functionality
print (number_of_counties['Munster'])
print (cities_of_provinces['NI'])


#print out every single item
for (province, number) in number_of_counties.items():
    print ('%s has %i counties' % (province, number)) 

#safely get an abbreviation of a state that isn't there
city = cities_of_provinces.get('Waterford', 'None')

if not city:
    print ('N\\A')




city = cities_of_provinces.get('Ulster', None)
if (not city):
    print ('It don\'t exist boah')
else:
    print (city)





#python using_dicts.py