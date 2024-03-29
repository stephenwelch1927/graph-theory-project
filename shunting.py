#Adapting code from Graph Theory class Shunting 
#Create a a function using shunting with operators in order of precedence



def shunt(infix):
    print("In Shunt")
    #Operator precedence higher the number what needs to be done 1st
    operPrec = {'*': 80, '?': 75, '+': 70, '.': 65, '|': 60, ')': 55, '(': 50}
    
    #Infix list 
    infix = list(infix)[::-1]

    #Operator stack
    operators = []

    #Postfix stack
    postfix = []

      # Loop through the input, one character at a time
    while infix:
        # Pop a character from the list
        c = infix.pop() # Removes the last element in infix as a list
                        # & returns whatever is poped off

        if c == '(':
            # Push an open bracket to the stack
            operators.append(c)
        elif c == ')':
            # Pop operators stack until open bracket is found
            while operators[-1] != '(':
                postfix.append(operators.pop())

            # Remove open bracket
            operators.pop()

        elif c in operPrec:
            # Push the operator stack until you find an open bracket
            while operators and  operPrec[c] < operPrec[operators[-1]]:
                # Push c to the operator stack with higher precidence to the output
                postfix.append(operators.pop())
            # Push c to the operator stack
            operators.append(c)
        else:
            # Typically we just push the character to the output
            postfix.append(c)

    # Pop all operators to the output
    while operators:
        postfix.append(operators.pop())
    # Convert output list to string
    return postfix
         

#print(f"postfix: {postfix}" )
# infix = "3+4*(2-1)"
# postfix = "3421-*+"

# print(f"Infix:  {infix}")
# print(postfix )