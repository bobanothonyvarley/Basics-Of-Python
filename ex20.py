#Here, I'm checking that .read does not automatically revert to the address of the first byte after 


from sys import argv

script, from_file, to_file = argv

#read from_file first, then write from file into to_file

#showing initial contents of .read
print (to_file.read())

current_file = open(from_file)
current_file_data = current_file.readline()

#should be at address of (final byte + 1) of fromfile now
second_file = open(to_file, 'w')
second_file.write(current_file_data)
#this should write one line into to_file

to_file.seek(0) #go back to address of first byte
print (to_file.read())







