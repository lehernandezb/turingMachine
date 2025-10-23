class turingMachine:
    def __init__(self, tape, blankSymbol = '_', startState = 'q0',acceptState = 'qAccept', rejectState = 'qReject', transitionFunction = None ):
        self.tape = list(tape)
        self.head = 0
        self.blank = blankSymbol
        self.start = startState
        self.accept = acceptState
        self.reject = rejectState
        transitionFunction = transitionFunction or {}