# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Noah Lawhorn
# Assignment Number: Lab#1
# Due Date: 09/05/2025
# Purpose: This program gives users a text based menu to choose 1 of 4 options which deals with input data and a buffer
# List Specific resources used to complete the assignment. Used W3Schools.com for syntax

# Sets the buffer to hold user input
buffer = ""

# Makes the program run infinite times until user exits
while True:

    # Displays menu and choices available
    print ("Data input buffer menu")
    print ("1. Enter Data")
    print ("2. Clear input buffer")
    print ("3. Display input buffer")
    print ("4. Exit program")

    # Allows user to input a command(number)
    choice = input("Enter your choice: ")

    # Option 1 takes a string and adds it to the buffer
    if choice == "1":
        data = input  ("Enter Text: ")
        buffer += data
        print ("Data Appended")

    # Option 2 clears the buffer
    elif choice == "2":
        buffer = ""
        print ("Buffer cleared")

    # Option 3 displays the buffer and current data inside of it
    elif choice == "3":
        if buffer == "":
            print ("Buffer empty")
        else:
            print (f"Current buffer data is: {buffer}")

    # Option 4 closes the program
    elif choice == "4":
        print("Program closed")
        break

    # If user inputs anything other than numbers 1-4
    else:
        print ("Invalid choice")
        continue


