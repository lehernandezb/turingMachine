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
    
    # Running machine
    def run(self, maxSteps=100):
        steps = 0

        # Stop when we reach a haulting state
        while self.state not in [self.accept, self.reject] and steps < maxSteps:
            self.step()
            steps += 1

            print(f"Step {steps}: {''.join(self.tape)} | Head at {self.head} | State: {self.state}")
        
        print("\nFinal result:")
        print(f"Tape: {''.join(self.tape)}")
        print(f"State: {self.state}")
        print(f"Result: {'ACCEPT' if self.state == self.accept_state else 'REJECT'}")

# Define the transtion function
transitionFunction = {

    #q0
    ('q0', 'a'): ('qA1', 'a', 'R'),
    ('q0', 'b'): ('qB1', 'b', 'R'),
    ('q0', '_'): ('qReject', '_', 'R'),
    
    #qA1
    ('qA1', 'a'): ('qA1', 'a', 'R'),
    ('qA1', 'b'): ('qA1', 'b', 'R'),
    ('qA1', '_'): ('qA2', '_', 'L'),

    #qA2
    ('qA2', 'a'): ('qAccept', 'a', 'R'),
    ('qA2', 'b'): ('qReject', 'b', 'R'),
    ('qA2', '_'): ('qReject', '_', 'R'),

    #qB1
    ('qB1', 'a'): ('qB1', 'a', 'R'),
    ('qB1', 'b'): ('qB1', 'b', 'R'),
    ('qB1', '_'): ('qB2', '_', 'L'),

    #qB2
    ('qB2', 'a'): ('qReject', 'a', 'R'),
    ('qB2', 'b'): ('qAccept', 'b', 'R'),
    ('qB2', '_'): ('qReject', '_', 'R'),

}

states = ['q0', 'qA1', 'qA2', 'qB1', 'qB2', 'qAccept', 'qReject']

tm = turingMachine(
    tape="aab",
    transitionFunction=transitionFunction
)

tm.run()
