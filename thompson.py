#Adapting code from Graph Theory class Thompson Construction
# A function that takes a regular expression and converts to an NFA

#Add a state to a set and follow all of the e arrows
def followes(state, current):
    if state not in current:
       # Put the state into current
        current.add(state)
       #See whether state is labeled by e
        if state.label is None:
            # Loop through the states pointed to by this one.
            for x in state.edges:
                # Follow all of their e(psilon)s too.
                followes(x, current) 

def match(regex, s):
    """Match function -> this  function will only return true if
        the regex matches the string, or else it will return false
    """

    # Compile the regular expression into an NFA
    nfa = compile(regex)
    
    # Try to match the regular expression to the string s
    # The current set of states
    current = set()
    # Add the first state and follow all epsilon arrows
    followes(nfa.start, current)
    # The previous set of states
    previous = set()

    # Loop through characters in s
    for c in s:
        # Keep track of where you were
        previous = current
        # Create a new empty set for the states we're about to be in
        current = set()
        # Loop through the previous states
        for state in previous:
            # Only follow arrows not labeled e(epsilon) 
            if state.label is not None:
                # If the label of the state is equal to the character we've read
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0], current)
                    
    # Ask the NFA if it matches the string s
    return nfa.accept in current