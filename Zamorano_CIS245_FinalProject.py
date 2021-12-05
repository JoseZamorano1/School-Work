import json
import requests
##We will call this to create a loop and menu for options.
def menu():
    print("\nEnter 1 to begin a weather forcast search...\n")
    print("Enter 0 to exit the program...")

#This will start the connection to the API and get the information from the customer
def api():
    #Test for Oregon
    zip = input('Enter a US ZipCode to display the weather data of that location. ')
    #Saving URL to make it look cleaner
    URL = 'https://api.openweathermap.org/data/2.5/weather?zip='+zip+',us&appid=a3365621fa2e45f06c6b45ac60b9c045'
    response = requests.get(URL)
    print("\n\nCONNECTION SUCCESFUL\n\n")
    print(response.text)
    
    
##Program needs try catch block, and program needs to be able to search by City Name

#Main that will run everything
def main():
    print("Hello, welcome to my final project!\n")## RENAME PLEASE
    #Calling Menu
    menu()
    #Int will be how the user decides what option they want
    choice = int(input("\nChoose an option..."))
    #Loop to keep the user in the program if they need to search multiple Zip Codes or City Names
    while choice != 0:
        if choice == 1:
            print("Search the weather per zipcode. ")
            api()
        else:
            print("Exit Program")
        menu()
        choice = int(input("\nChoose an option...\n"))
    print("Closing the program...")

main()
