
import thompson, menu, shunting, sys
def runner():
    while True:
        postfix = " "
       # myInfix = " "
        myString = " "
        option = menu.menu()
        if option == "1":
            #infix = "3+4*(2-1)"
            myInfix = input("Enter Infix Expression: ")
        elif option == "2":
            myString = input("Enter String: ")
            postfix = shunting.shunt(myInfix)
            print(f"postfix: {postfix}" )
        else:
            sys.exit()
    
runner()