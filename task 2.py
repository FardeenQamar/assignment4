user_in = input('''Enter the data : ''')

file_write = open('output.txt', 'w')
file_write.write(user_in + '\n')
print("Data has been written successfully to output.txt \n ")
file_write.close()

new_user_in = input('Enter additional data to append to same file : ')

file_append = open('output.txt','a')
file_append.write(new_user_in)
print('New data has been appended successfully to output.txt \n ')
file_append.close()


with open('output.txt','r') as read_me:
    read1 = read_me.readlines()

print('The final content of the file are :')

for i in read1:
    print(i.strip('\n'))


