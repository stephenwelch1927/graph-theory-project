#Adapting code from Graph Theory class Shunting and added State, NFA and re_to_NFA
#Create a a function using shunting with operators in order of precedence



def shunt(infix):
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

class State:
    
    # constructor
    def __init__(self, label, arrows, accept):
        self.label = label
        self.arrows = arrows
        self.accept = accept

    # followes e's
    def followes(self):
        '''The set of states that are gotten from following this state and all its e arrows'''
        # include this state in the returned set
        states = {self}

        # if this state has e arrows 
        if self.label is None:
            # loop through this state's arrows
            for state in self.arrows:
                # incorporates that state's e arrow states in states
                states = (states | state.followes())
        
        # returns the set of states
        return states


class NFA:
   
    """ NFA class to represent the whole NFA """
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    # Match Function
    def match(self, s):
        '''return True iff this NFA (instance) matches the string'''
        # create a list of previous states that we are still in
        previous = self.start.followes() 

        # loop through the string a character at a time
        for c in s:
            # start with empty set of current states
            current = set()
            # loop through the previous states
            for state in previous:
                # check if there is a c arrow from state
                if state.label == c:
                    # add followes for next state
                    current = (current | state.arrows[0].followes())
            
            # replace previous with current
            previous = current
         
        return (self.end in previous)

def re_to_nfa(postfix):
    # a stack for NFA's, list of pointers to instances of class NFA
    stack = []
    # loop through the postfix regexe left to right
    for c in postfix:
        # concatenation
        if c == '.':
            # pop two fragments off the stack
            # pop top NFA off stack
            nfa2 = stack[-1] 
            stack = stack[:-1] 
            # pop the next NFA off stack
            nfa1 = stack[-1] 
            stack = stack[:-1]
            # make accept state of nfa1 non-accept
            nfa1.end.accept = False
            # make it point at start state of nfa2
            nfa1.end.arrows.append(nfa2.start) 
            # create new NFA with nfa1's start state and nfa2's end state
            nfa = NFA(start=nfa1.start, end=nfa2.end)
            # push to the stack
            stack.append(nfa)
        elif c == '|':
            # pop two fragments off the stack            
            # pop top NFA off stack
            nfa2 = stack[-1]
            stack = stack[:-1] 
            # pop the next NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # create new start and end states
            start = State(label=None, arrows=[], accept=False)
            end = State(label=None, arrows=[], accept=True)
            # make new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # make old accept states non-accept
            nfa1.end.accept = False
            nfa2.end.accept = False
            # point old end states to new one
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # make a new NFA
            nfa = NFA(start, end)
            # push to the stack
            stack.append(nfa)
        elif c == '*':            
            # pop one NFA off stack
            nfa1 = stack[-1] 
            stack = stack[:-1]
            # create new start and end state
            start = State(label=None, arrows=[], accept=False)
            end = State(label=None, arrows=[], accept=True)
            # make new start state point at old start states
            start.arrows.append(nfa1.start)
            # and at the new end start
            start.arrows.append(end)
            # make old end state non-accept
            nfa1.end.accept = False
            # make old state point to new end state
            nfa1.end.arrows.append(end)
            # make old end state point to old start state
            nfa1.end.arrows.append(nfa1.start)
            # make a new NFA
            nfa = NFA(start, end)
            # push to the stack
            stack.append(nfa)
        else:
            # create an NFA for the non-special character c
            # create the end state
            end = State(label=None, arrows=[], accept=True)
            # create the start state, pointed at the end state
            start = State(label=c, arrows=[end], accept=False)
            # point new start state at new end state
            start.arrows.append(end)
            # create the NFA with the start and end state
            nfa = NFA(start=start, end=end)
            # append the NFA to the NFA stact
            stack.append(nfa)  
    # should only be one instance of an NFA on the stack
    if len(stack) !=1:
        return None
    else:
        return stack[0]
         

#print(f"postfix: {postfix}" )
# infix = "3+4*(2-1)"
# postfix = "3421-*+"

# print(f"Infix:  {infix}")
# print(postfix )