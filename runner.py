import thompson, menu, shunting, sys

def runner():
    while True:
        postfix = " "
        myString = " "
        option = menu.menu()
        if option == "1":
            infix = input("Enter Infix Expression: ")
        elif option == "2":
            myString = input("Enter String: ")
            print(f"infix: {infix}")
            print(f"string: {myString}")
            postfix = shunting.shunt(infix)
            nfa = shunting.re_to_nfa(postfix)
            match = nfa.match(myString)
            print(f"Match '{myString}': {nfa.match(myString)}")
            print()
        else:
            sys.exit()
# Run the program call to function
runner()