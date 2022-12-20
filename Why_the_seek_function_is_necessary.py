#Here, I'm checking that .read does not automatically revert to the address of the first byte after execution


from sys import argv

script, from_file, into_file = argv

#read from_file first, then write from_file into into_file

#showing initial contents of into_file
print (into_file.read())

current_file = open(from_file)
current_file_data = current_file.readline()

#should be at address of (first byte of second line) of fromfile now
second_file = open(into_file, 'w')
second_file.write(current_file_data)
#this should write at the start of the second line of into_file

print (into_file.read())
#compare the difference






