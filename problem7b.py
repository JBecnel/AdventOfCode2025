file_name = "input7.txt"
with open(file_name, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        print(line)

position = lines[0].find("S")
print(f"Position of 'S': {position}")

tacs = {position : 1}

for line in lines[1:]:    
    tac_list = list(tacs.keys())
    for tac in tac_list:        
        if line[tac] == '^':
            if (tac - 1) >= 0:
                if tac -1 not in tacs:
                    tacs[tac - 1] = tacs[tac]
                else:
                    tacs[tac - 1] += tacs[tac]
            if (tac + 1) < len(line):
                if tac + 1 not in tacs:
                    tacs[tac + 1] = tacs[tac]
                else:
                    tacs[tac + 1] += tacs[tac]
            tacs.pop(tac)
    print(line)
    print(tacs)

total_tacs = sum(tacs.values())
    

print("Final positions of 'TAC':", tacs)
print("Number of 'Timelines':", total_tacs)
    