# Create an options menu for user

def menu():
    print("*******************************************")
    print("       RegEx Converter                     ")
    print(" Enter 1. For Infix Regexe                 ")
    print(" Enter 2. For String to match Infix Regexe ")
    print(" Enter 3. Exit App                         ")
    print("*******************************************")

    userInput = input("Enter Menu Option: ")
    print("User Entered", userInput)
    return userInput