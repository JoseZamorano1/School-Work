#Jose Zamorano, 09 December 2021
# Assignment 8.1 | File System Program

import os
#Try catch block to validate if that directory exists to put stuff in.
##Try Catch block to validate wether the file exists.

#print(os.getcwd())


#Main will run everything.
def main():
    #Welcome User to program. 
    print("\nWelcome to the file directory program!\n")
    #Get the location of the directory.
    directory = input("\nEnter the directory where you would like to save this file... \n"
    + "\nExample of a valid directory: >>'C:/Users/New User/Desktop/test/'<< ")
    #Try catch block in case the directory already exists.
    try:
        #Making the directory.
        os.mkdir(directory)
    except:
        
        print("You input the file name incorrectly, try again.")
    #Getting the file name of the directory.
    fileName = input("\n\nEnter the name of your file name..."
    +"\n Example of a valid file name: >>'test.txt'<<\n\n")
    #Getting all the information from the user to add to the text file.
    name = input("\n\nEnter your name... \n\n")
    address = input("\n\nEnter your address... \n\n")
    phoneNumber = input("\n\nEnter your phone number...\n\n")
    #making the full path of the file here.
    fullPath = directory+fileName
    
    try:
       #Here is where we append to the file by adding name, address, phone number.
        manipulateFile = open(fullPath, "a+")
        manipulateFile = manipulateFile.write(name + ", " + address + ", " + phoneNumber)
        manipulateFile.close()

    except: 

        pass
    
    #Reading and printing from the file to display contents to the user.
    readFile = open(fullPath, "r")
    data = readFile.read()
    print(data)
    
#Calling main to run the program.
main()

