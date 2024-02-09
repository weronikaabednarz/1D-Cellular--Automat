import numpy as np

def split_into_pairs(number):
    change_into_string = str(number)
    pairs = []
    for i in range(0, len(change_into_string), 2):
        pair = int(change_into_string[i:i+2])
        pairs.append(pair)
    return pairs

def cellular_automaton(rule, time, base_cells, boundary_condition):
    if time <= 0:
        print("Czas musi być większy od 0")
        return
        
    else:
        binary_rule = bin(rule)
        temp = ""
        for i in range (8-len(binary_rule[2:])):
            temp += "0"
        
        print(base_cells)
        binary_rule = temp + binary_rule[2:]

        
        plik = open(f'Rule{rule}.txt',"w")
        for t in range (time):
            new_tab = np.zeros(len(base_cells), dtype=int)
            for i in range (len(base_cells)):
                zero_cell = ""
                for j in range(-1,2):
                    if boundary_condition == 'absorpcyjny':
                        if i + j > len(base_cells)-1 or i + j < 0:
                            zero_cell += "0" 
                        else:
                            zero_cell += str(base_cells[i+j])
                    else:
                        zero_cell += str(base_cells[(i+j+len(base_cells))% len(base_cells)])

                zero_cell = 7- int(zero_cell,2) 
                new_cell = binary_rule[zero_cell]
                new_tab[i] = new_cell
            plik.write(np.array2string(new_tab)+"\n")
            linia = np.array2string(new_tab)
            linia = linia.replace("0"," ")
            linia = linia.replace("1","\u25A0")
            print(linia)

            base_cells = new_tab
        plik.close()



numer_albumu = 410023 
pairs = split_into_pairs(numer_albumu)

print("Numer albumu:", numer_albumu)
print("Pary liczb:", pairs)
base = np.array([1,1,0,0,1,0,1,0,0,1,1], dtype=int)

print("warunek brzegowy absorpcyjny:")
cellular_automaton(90, 5, base,'absorpcyjny')
print("warunek brzegowy periodyczny:")
cellular_automaton(90, 5, base, 'periodyczny')


for n in pairs:
    print("Dla numeru albumu:")
    cellular_automaton(n, 5, base, "absorpcyjny")