class turingMachine:

    # Defining the turing machine
    def __init__(self, tape, states, blankSymbol = '_', startState = 'q0', acceptState = 'qAccept', rejectState = 'qReject', transitionFunction = None ):
        self.tape = list(tape)
        self.head = 0
        self.states = list(states)
        self.blank = blankSymbol
        self.start = startState
        self.accept = acceptState
        self.reject = rejectState
        self.delta = transitionFunction or {}

    # Computing the step in the machine
    def step(self):

        #Make sure tape is in bounds
        if self.head < 0:
            self.tape.insert(0, self.blank)
        elif self.head  >= len(self.tape):
            self.tape.append(self.blank)

        symbol = self.tape[self.head]
        key = (self.state, symbol)

        # If not transition function is defined, reject
        if key not in self.delta:
            self.state = self.reject
            return
        
        newState, newSymbol, move = self.delta[key]

        if move == "R":
            self.head += 1
        elif move == "L":
            self.head -= 1
        elif move == "S":
            pass
    

    