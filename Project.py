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



if len(sys.argv) < 2:
    print("Please insert a valid path to MIPS file") 
    exit(0)

pathToFile = sys.argv[1]

REs = {
    # (r'\b(?:lw|add|sw)\b') : "Instructions" ,
    r"lw":"load", r"sw" : "store", r"add|ADD":"add",
    r"sub|SUB": "sub",
    r"mul|MUL": "mul",
    r"div|DIV": "div",
    r"and|AND": "and",
    r"or|OR": "or",
    r"nor|NOR": "nor",
    r"xor|XOR": "xor",
    r"slt|SLT": "Set on Less Than",
    r"beq|BEQ": "BranchifEqual",
    r"bne|BNE": "BranchNotEqual",
    r"^[j|J]": "jump",
    r"jal|JAL": "JumpandLink",
    r"jr|JR": "JumpRegister",
    r"slti|SLTI": "SetonLessThanImmediate",
    r"sltu|SLTU": "SetonLessThanUnsigned",
    r"sltiu|SLTIU": "SetonLessThanImmediateUnsigned",
    r"sll|SLL": "ShiftLeftLogical",
    r"srl|SRL": "ShiftRightLogical",
    r"li|LI": "LoadImmediate",
    r"syscall|SYSCALL": "SystemCall",
    r"l.s": "LoadSingle(floating-point)",
    r"s.s": "StoreSingle(floating-point)",
    r"add.s": "AddSingle(floating-point)",
    r"sub.s": "SubtractSingle(floating-point)",
    r"mul.s": "MultiplySingle(floating-point)",
    r"div.s": "DivideSingle(floating-point)",
    r"lui": "LoadUpperImmediate",  
    r"^\$": "register",
    r"^[a-zA-Z]\w*":"identifier",
    r"mv|MV": "move",
    r"\d+": "number"
}


file = open(pathToFile, "r")


lex = []    # list of resulting lexemes (add to it)
for line in file:
    if re.search(r"#.*", line):
        lex.append((line, "comment"))
        continue
    elif re.search(r"$:", line):
            idx = line.index(":")
            lex.append((line[:idx], "Label"))
            line = line[idx+1:]
            if len(line.split())==0:
                continue
    for element in line.split():  # for each token in the line after splitting
        for key in REs.keys():  # to look for matching REs in the dictionary
            if re.search(key, element) != None: #and flag ==0:
                if  ',' in element:
                    lex.append((REs[key], element[:-1]))
                    lex.append(("comma", ","))
                    break
                if ':' in element:
                    lex.append((REs[key], element[:-1]))
                    lex.append(("colon", ":"))
                    
                else:
                    lex.append((REs[key], element))
                    break

                

                
"""
we make the cfg as follows:
    just put a punch of if conditions
    and use them to check the if the syntax is correct?
    suggestion: make the tree along the conditions if possible

    template for the if conditions:
        !groups of instructions to be checked **main if condition**
            split them based on the type of input next. if registers or identifier
                check for commas, check for the end token, the final identifier/register

        
"""
for key , val in lex:
    print(f"{key}, {val}")
print()


def checkSyntax(SlicedList, Grammar):
    if len(SlicedList) ==0:
        return
    print(f"|  |  |  |--Operands")
    for i in range(len(Grammar)):
        print(f"|  |  |  |  |--{SlicedList[i][0]}: {SlicedList[i][1]}")
        if SlicedList[i][0] != Grammar[i]:
            raise Exception(f"Expected: {Grammar[i]} but found: {SlicedList[i]}")



def syntaxParser(LexTokens):
    # we will put all the instructions in a list here so its easier to manage
    RType = ["add", "sub", "lw", "and", "or", "mv", "nor", "xor"]
    IType = ["addi", "subi", "sw"]
    Branch = ["beq", "bne"]
    S = [RType, IType, Branch]
    RTypeSyntax = ["register", "comma", "register"]
    ITypeSyntax = ["register", "comma", "register", "comma", "number"]
    BranchSyntax = ["register", "comma", "register", "label"]

    print("Program\n|--TextSection")
    
    
    Idx = 0
    while Idx < len(LexTokens):
        if LexTokens[Idx][1] in RType:
            print(f"|  |  |--{LexTokens[Idx][0]} Instructions")
            print(f"|  |  |  |--{LexTokens[Idx][0]}: {LexTokens[Idx][1]}")
            Idx+=1
            checkSyntax(LexTokens[Idx:Idx+3], RTypeSyntax)

            Idx+=3
        elif LexTokens[Idx][1] in IType:
            print(f"|  |  |--{LexTokens[Idx][0]} Instructions")
            print(f"|  |  |  |--{LexTokens[Idx][0]}: {LexTokens[Idx][1]}")
            Idx+=1
            checkSyntax(LexTokens[Idx:Idx+6], ITypeSyntax)

            Idx+=6
        elif LexTokens[Idx][1] in Branch:
            print(f"|  |  |--{LexTokens[Idx][0]} Instructions")
            print(f"|  |  |  |--{LexTokens[Idx][0]}: {LexTokens[Idx][1]}")
            Idx+=1
            checkSyntax(LexTokens[Idx:Idx+6], BranchSyntax)
           
            Idx+=6
        elif LexTokens[Idx][1] == "label":
            print(f"|  |  |--{LexTokens[Idx][0]} Instructions")
            print(f"|  |  |  |--{LexTokens[Idx][0]}: {LexTokens[Idx][1]}")
            Idx+=1
            continue
        elif LexTokens[Idx][1] == "comment":
            Idx+=1
            continue
        else:
            raise Exception(f"Expected an instruction or a label got: {LexTokens[Idx][1]} ")
    print(f"|--Exit")

                
syntaxParser(lex)
