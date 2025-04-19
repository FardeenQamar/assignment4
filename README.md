# assignment4
task1 :
  I used try and except to handle error 
  I then used a file named sample file as txt file and then open it with 'with' so that i dont have to close the file manually and it is dne under try: (block)
  Then as instructions i open the file as read only and also used 'read' method assigned it to a variable named read me
  Then I assigned read1.redlines() as read2 so that it will give me a list of all the lines in the txt file
  I then used a counter to assign teh label of each line as ( line 1 , line 2)etc.
  To get each line separately i used 'for' to iterate over the list (read1)
  but the list contains [\n] so to remove it i used strip method
  cuz for loop automatically gives next line to the next character or word or object in a list 
  now i just used formatted string to print line no and the line of sample txt

  Then i used except :
    to handle error like filenotfounderror cuz it is read only
    


task 2 :
  I asked the user to input data in a file 
  I then open the file as write only and assign it to file write and used 'write' method inside which i also gave'\n' so that the next data can be added systematically line by line
  and printed that data has been added
  I then asked again for user to input data append 
  and now open the file as append only and used similar concept as above 
  and printed data has been appended
  and also you have to close file every time so I did 
  And finally i read the added and appended data with open and read file as read only and use readlines to get a list of the data
  then printed a string as the final data of the file is :
  then i used same cocept of task1 and used for loop to iterate the list and print the lines adn strip [\n]
  





  
  
