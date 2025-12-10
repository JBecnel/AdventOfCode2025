
def parse_input(filename):
    states = [ ]
    schematics = [ ]
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Parse the first part (before first space)
            parts = line.split(']')
      
            # Parse the numbers in parentheses
            numbers_part = parts[1]
            numbers = numbers_part.split(")")            

            desired_state = numbers[-1] # last entry is the desired state
            desired_state = desired_state[2:len(desired_state)-1] # remove first and last { }
            #print(desired_state)
            desired_state = tuple(int(c) for c in desired_state.split(","))
            
            states.append(desired_state)
            numbers = numbers[:-1] # remove last entry
            #print(numbers)
            wiring = [ ]
            for seq in numbers:
                pattern = seq[2:] # ignore first " ("
                buttons = pattern.split(",")
                button_list = [False] * len(desired_state)
                for b in buttons:
                    for wire in b:
                        button_list[int(wire)] = True

                wiring.append(tuple(button_list))

            schematics.append(wiring)

            

          
            
    return states, schematics

def press_button(state, button):
    new_state = tuple(state[i]+1 if button[i] else state[i] for i in range(len(state)))
    return new_state

def is_valid(new_state, final_state):
    for i in range(len(new_state)):
        if new_state[i] > final_state[i]:
            return False
    return True

def find_fewest_clicks(final_state, buttons):
    start = tuple(0 for _ in range(len(final_state)))
    states = { start : 0}         
    new_states = {start}
    
    final_state_found = False
    while not final_state_found:
        states_next_round = set()
        for state in new_states:
            for button in buttons:
                new_state = press_button(state, button)
                #print(new_state)
                if is_valid(new_state, final_state) and (new_state not in states):
                    states[new_state] = states[state] + 1
                    states_next_round.add(new_state)
                if final_state == new_state:
                    final_state_found = True
                    break
            if final_state_found:
                break
        new_states = states_next_round

    return states[final_state]

final_state, buttons = parse_input('sample_input10.txt')
total = 0
for i in range(len(final_state)):
    print(final_state[i], " : ", buttons[i ])
    clicks = find_fewest_clicks(final_state[i], buttons[i])
    print(clicks)
    total += clicks

print(total)

# final_state, buttons = parse_input('input10.txt')
# total = 0
# for i in range(len(final_state)):
#     print(final_state[i], " : ", buttons[i ])
#     clicks = find_fewest_clicks(final_state[i], buttons[i])
#     print(clicks)
#     total += clicks

# print(total)