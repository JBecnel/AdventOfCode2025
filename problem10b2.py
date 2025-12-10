from z3 import *

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

def solve_system(buttons, b):
    vars = [ ]
    for i in range(len(buttons)):
        vars.append(Int("x" + str(i)))

    
    opt = Optimize()
    for i in range(len(b)):
        constraint = 0
        for j in range(len(buttons)):
            button = buttons[j]
            if button[i]:
                if constraint == 0:
                    constraint = vars[j]
                else:    
                    constraint += vars[j]
        opt.add(constraint == b[i])

    for v in vars:
        opt.add(v >= 0)
    
    obj = vars[0]
    for i in range(1,len(vars)):
        obj = obj + vars[i]
    
    opt.minimize(obj)    
    if opt.check() == sat:
        sol = opt.model()
        
        #print(opt)
        #print(sol)

    total = 0
    for v in vars:
        total = total + sol[v].as_long()

    
    return total
    

    
final_state, buttons = parse_input('sample_input10.txt')
total = 0
for i in range(len(final_state)):
    #print(final_state[i], " : ", buttons[i ])
    clicks = solve_system(buttons[i], final_state[i])
   #print(clicks)
    total += clicks

print(total)


final_state, buttons = parse_input('input10.txt')
total = 0
for i in range(len(final_state)):
    #print(final_state[i], " : ", buttons[i ])
    clicks = solve_system(buttons[i], final_state[i])
    #print(clicks)
    total += clicks

print(total)



# from z3 import *

# # Create an optimizer instance
# opt = Optimize()

# # Declare integer variables
# x = Int('x')
# y = Int('y')

# # Add constraints
# opt.add(x >= 0)
# opt.add(y >= 0)
# opt.add(x + y >= 10)
# opt.add(2*x + y <= 20)

# # Define the objective function to minimize
# objective = 3*x + 2*y
# opt.minimize(objective)

# # Check for satisfiability and get the model
# if opt.check() == sat:
#     model = opt.model()
#     print(f"Optimal x: {model[x]}")
#     print(f"Optimal y: {model[y]}")
#     print(f"Minimum objective value: {model.evaluate(objective)}")
# else:
#     print("Problem is unsatisfiable.")