#Adapting code from Graph Theory class Shunting 
#Create a a function using shunting with operators in order of precedence



def shunt(infix):
    #Operator precedence higher the number what needs to be done 1st
    operPrec = {'*': 80, '?': 75, '+': 70, '.': 65, '|': 60, ')': 55, '(': 50}
    
    #Infix list 
    infix = list(infix)[::-1]

    #Operator stack
    operators = []

    #Postfix stack
    postfix[]

      # Loop through the input, one character at a time
    while infix:
        # Pop a character from the list
        c = infix.pop() # Removes the last element in infix as a list
                        # & returns whatever is poped off

        if c == '(':
            # Push an open bracket to the stack
            opers.append(c)
        elif c == ')':
            # Pop operators stack until open bracket is found
            while opers[-1] != '(':
                postfix.append(opers.pop())

            # Remove open bracket
            opers.pop()

        elif c in prec:
            # Push the operator stack until you find an open bracket
            while opers and  prec[c] < prec[opers[-1]]:
                # Push c to the operator stack with higher precidence to the output
                postfix.append(opers.pop())
            # Push c to the operator stack
            opers.append(c)
        else:
            # Typically we just push the character to the output
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string
    return ''.join(postfix)
         


while there are tokens to be read:
    read a token.
    if the token is a number, then:
        push it to the output queue.
    else if the token is a function then:
        push it onto the operator stack 
    else if the token is an operator then:
        while ((there is an operator at the top of the operator stack)
              and ((the operator at the top of the operator stack has greater precedence)
                  or (the operator at the top of the operator stack has equal precedence and the token is left associative))
              and (the operator at the top of the operator stack is not a left parenthesis)):
            pop operators from the operator stack onto the output queue.
        push it onto the operator stack.
    else if the token is a left parenthesis (i.e. "("), then:
        push it onto the operator stack.
    else if the token is a right parenthesis (i.e. ")"), then:
        while the operator at the top of the operator stack is not a left parenthesis:
            pop the operator from the operator stack onto the output queue.
        /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
        if there is a left parenthesis at the top of the operator stack, then:
            pop the operator from the operator stack and discard it
        if there is a function token at the top of the operator stack, then:
            pop the function from the operator stack onto the output queue.
/* After while loop, if operator stack not null, pop everything to output queue */
if there are no more tokens to read then:
    while there are still operator tokens on the stack:
        /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        pop the operator from the operator stack onto the output queue.
exit.

infix = "3+4*(2-1)"