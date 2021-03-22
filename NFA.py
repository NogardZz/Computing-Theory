class NFA():
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return

    def transition_to_state_with_input(self, input_value):
        res = set()
        for sub_state in self.current_state:
            if ((sub_state, input_value) not in self.transition_function.keys()):
                continue
            res.update(self.transition_function[(sub_state, input_value)])
        self.current_state = res
        return

    def in_accept_state(self):
        for sub_state in self.current_state:
            if sub_state in self.accept_states:
                return True
        return False

    def go_to_initial_state(self):
        self.current_state = {self.start_state}
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()

if __name__ == "__main__":
    automat = NFA(
        {0, 1, 2, 3, 4},
        {'0', '1'},
        dict({
            (0, '0'): {0, 2},
            (0, '1'): {0, 1},
            (1, '1'): {2},
            (2, '0'): {2},
            (2, '1'): {2},
            (3, '0'): {4},
            (4, '0'): {4},
            (4, '1'): {4}
        }),
        0,
        {2, 4}
    )

    print(automat.run_with_input_list(list('00')))
