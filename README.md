# PythonHub
Mini Project - A Simple Quiz Website Built In Python 


### Description
This program is a simple user account system that allows users to create, login, and logout of their accounts. The program utilizes the re (regular expressions) module to ensure that users enter valid email addresses when creating an account, and a dictionary to store user data.

The createAccount function prompts the user to enter their email, username, and password, and checks if the email and username are already in use. If the email address is not in the correct format, the user is prompted to enter a valid email address.

The loginAccount function prompts the user to enter their email and password, and checks if the entered email and password match a user in the users dictionary. If the email and password match, the user is logged in and their username and email are displayed. If the email and password do not match, an error message is displayed.

The logout function allows a user to delete their account by entering their email. If the email is not found in the users dictionary, an error message is displayed. Additionally, the program contains a rule function that provides information about the game and instructions on how to create and login to an account.

The rules function is defined, which provides information about the game, such as the number of questions, point system, and instructions on how to create and login to an account.

The play function is defined, which welcomes the user and prompts them if they are ready to play the game. If the user enters "Yes", the game will begin, otherwise the game will not start.

The if __name__ == "__main__" statement is a way to ensure that the code in this block only runs when the script is executed directly and not when imported as a module.This code is a simple menu system that allows users to interact with the program by selecting options from a list. The menu is displayed in a while loop, which continues to run until the user selects option 6, "EXIT". The code allows the user to navigate through various options and interact with the system in a user friendly way.

The code is well-organized and easy to understand, making it easy to modify and customize to fit specific needs.The program is useful tool for anyone looking to implement a basic user account system in their application, it's a good starting point for building more complex systems.
