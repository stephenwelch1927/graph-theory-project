
class State:
    def __init__(self, accept, arrows):
        # True if this is an accept state.
        self.accept = accept
        # Arrows (keys are labels) out of state.
        self.arrows = arrows

class DFA:
    """An Automaton"""
    def __init__(self, start):
        #Start state of Automaton
        self.start = start
    
    def match(self, s):
        """See is s is accepted by automaton"""
        # Current state
        current = self.start
        # Loop through the characters in s
        for c in s:
            # find the state in arrows with key c
            current = current.arrows[c]
            # Return whether we're in accept state
            return current.accept

def compile():
    """Create Automatom"""

    # Create the start state
    start = State(True, {})
    # Create the other state
    other = State(False, {})

    # The states point to themselves on a 0
    start.arrows['0'] = start
    other.arrows['0'] = other

    # The states point to themselves 
    start.arrows['1'] = other
    other.arrows['1'] = start

    # Create an automaton
    parity = DFA(start) 

    # Return automaton
    return parity
# Create automaton instance
myAutomaton = compile()
for s in ['1100', '11111', '', '1', '0']:
    # Check if s is accepted by the automaton.
    result = myAutomaton.match(s)
    print(f"{s} -> {result}")     

