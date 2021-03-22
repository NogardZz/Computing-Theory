class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function #Kieu tu dien co key(), co value
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
#Kiem tra xem ki hieu ke tiep la ki hieu gi?
    def transition_to_state_with_input(self, input_value): #Di chuyen sang trang thai moi khi nhan vao 1 ky tu
        if (self.current_state, input_value) not in self.transition_function.keys():
            #key() co trang thai doc vao ki hieu nhap
            #value tuong ung voi key la trang thai chuyen qua
            self.current_state = None
            return
        #neu ton tai duong di
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state() #Gan trang thai hien tai
        for inp in input_list: #Lay cac ky tu trong chuoi input_list
            self.transition_to_state_with_input(inp) #Truyen tham so inp vao
            continue
        return self.in_accept_state()

    pass


states = {0, 1, 2}
alphabet = {'0', '1'} #bo chu cai nhap
start_state = 0 #Trang thai dau
accept_states = {0} #Dang tap hop(Trang thai ket thuc)
#Bang chuyen trang thai
tf = dict()
tf[(0, '0')] = 0
tf[(0, '1')] = 1
tf[(1, '0')] = 2
tf[(1, '1')] = 0
tf[(2, '0')] = 1
tf[(2, '1')] = 2


d = DFA(states, alphabet, tf, start_state, accept_states)
print(type(alphabet)) #Doc kieu du  lieu
inp_program = input("Nhap vao chuoi: ")

print(d.run_with_input_list(inp_program))
