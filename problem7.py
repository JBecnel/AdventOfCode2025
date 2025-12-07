with open('input7.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        print(line)

position = lines[0].find("S")
print(f"Position of 'S': {position}")

tacs = {position}
count = 0
for line in lines[1:]:    
    tac_list = list(tacs)
    for tac in tac_list:        
        if line[tac] == '^':
            count += 1
            tacs.remove(tac)
            if (tac - 1) >= 0:
                tacs.add(tac - 1)
            if (tac + 1) < len(line):
                tacs.add(tac + 1)
    #print(line)
    #print(list(tacs))

        
    

print("Final positions of 'TAC':", tacs)
print("Number of 'TAC's:", len(tacs))
print("Number of '^' encountered:", count)