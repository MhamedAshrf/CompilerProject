""" 
    IMPORTANT!!!!!!!!!!!!!!!!!!!
    in order for this code to work please add an argument during the file running
    indicating the path of the MIPS code file for the code to read as such:
                    python3 phase1.py /path/to/MIPS/file.txt

Names and IDs
Mohammed Ashraf Abdulsami 202002700
Omar Alaa Abdelrasoul     202002224
Omar Mamdouh Shaban     202001125
Seif Eldin Wael Samir      202002249
"""





import re
import sys



# def 

pathToFile = sys.argv[1]

REs = {
    # (r'\b(?:lw|add|sw)\b') : "Instructions" ,
    r"lw":"load", r"sw" : "Store", r"add":"Add",
    r"sub": "Subtract",
    r"mul": "Multiply",
    r"div": "Divide",
    r"and": "Bitwise AND",
    r"or": "Bitwise OR",
    r"nor": "Bitwise NOR",
    r"xor": "Bitwise XOR",
    r"slt": "Set on Less Than",
    r"beq": "Branch if Equal",
    r"bne": "Branch if Not Equal",
    r"j": "Jump",
    r"jal": "Jump and Link",
    r"jr": "Jump Register",
    r"slti": "Set on Less Than Immediate",
    r"sltu": "Set on Less Than Unsigned",
    r"sltiu": "Set on Less Than Immediate Unsigned",
    r"sll": "Shift Left Logical",
    r"srl": "Shift Right Logical",
    r"li": "Load Immediate",
    r"syscall": "System Call",
    r"l.s": "Load Single (floating-point)",
    r"s.s": "Store Single (floating-point)",
    r"add.s": "Add Single (floating-point)",
    r"sub.s": "Subtract Single (floating-point)",
    r"mul.s": "Multiply Single (floating-point)",
    r"div.s": "Divide Single (floating-point)",
    r"lui": "Load Upper Immediate",  
    r"^\$": "register",
    r"[a-z-A-Z]+\w*":"identifier"
}


file = open(pathToFile, "r")


flag =0     # to stop looking for further matches in the dict of REs
lex = []    # list of resulting lexemes (add to it)
for line in file:
    for element in line.split():  # for each token in the line after splitting
        # flag = 0            # reset flag
        for key in REs.keys():  # to look for matching REs in the dictionary
            if re.search(key, element) != None: #and flag ==0:
                if  ',' in element:
                    lex.append((REs[key], element[:-1]))
                    lex.append(("comma", ","))
                    break

                else:
                    lex.append((REs[key], element))
                    break
                # if re.search(",", element) != None:
                #     lex.append(("comma", ","))
                #     break;
                

# print lexemes
for x,y in lex:
    print(f'Token:{x}, Lexeme: {y}\n')
print("Symbol Table:")
for x,y in lex:
    if x == "identifier":
        print(f'-Name: {y}, Type: Memory address')
        


