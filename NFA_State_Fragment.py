# Class created for Fragment and state to represent NFA

class State:
        """ A state with one or two arrows, all edges labeled by label. """
        # Every state has 0, 1, or 2 edges from it.
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        #Label for the arrows, None means epsilon.
        self.label = label

class Fragment:
    """ An NFA fragment with a start state and an accept state"""
    #Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept