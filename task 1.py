filename = 'sample.txt'

try:
    #read_me = open('sample.txt','r') you can use this as well but you have to close file with an ectra line of code 
    with open('sample.txt','r') as read_me:
        read1 = read_me.readlines()
        counter = 0
        for i in read1:
            counter += 1
            read2 = str(i)
            read3 = read2.strip('\n')

            print(f'Line{counter}: {read3}')
except FileNotFoundError :
    print(f'The file {filename} does not exist')


    
   


