# READING A FILE
# open the file to interaction
my_file = open('data.txt', 'r')
# extract content to safely close the file in next step while having the data
data = my_file.read()
my_file.close()

print(data)

# WRITING TO A FILE
user_name = input('Enter your username: ')
my_file_writing = open('data.txt', 'w')
# use the .write method but erases original content
my_file_writing.write(user_name)

my_file_writing.close()