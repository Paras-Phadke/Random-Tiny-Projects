inta = input("enter input(element,mol,vol,gram,atom,mlc) = ")
elelist=["H","He","C","N","O","Na","Mg","Al","P","S","Cl","K","Ca"]
tpoi = ""
na = 6.02e23
stp = 22.4
nummol = 0
numvol = 0
numgram = 0
numatom = 0
nummlc = 0
mm = 0
elementsgram = {
    "H":1,
    "He":2,
    "C":12,
    "N":14,
    "O":16,
    "Na":23,
    "Mg":24,
    "Al":27,
    "P":31,
    "S":32,
    "Cl":35.5,
    "K":39,
    "Ca":40
}
eleininta = []

def elinum(inta:str):
    for i in range(0,len(elelist)):
        if inta.count(elelist[i]) == 1:
            inde = inta.index(elelist[i])
            if inta[inde + 1].isdigit():
                for i in range(0, int(inta[inde + 1])):
                    eleininta.append(elelist[i])
                    inta.strip(elelist[i])
            elif  inta[inde + 2].isdigit():
                for i in range(0, int(inta[inde + 2])):
                    eleininta.append(elelist[i])
                    inta.strip(elelist[i])
            else:
                eleininta.append(elelist[i])
                inta.strip(elelist[i])
    inta.strip()
    return inta

def stripper(inta:str):
    inta.replace("mol","")
    inta.replace("gram","")
    inta.replace("vol","")
    for i in range(0,len(elelist)):
        if inta.count(elelist[i]) == 1:
            inde = inta.index(elelist[i])
            if inta[inde + 1].isdigit():
                inta.replace(inta[inde+1],"")
            elif inta[inde + 2].isdigit():
                inta.replace(inta[inde+2],"")
            inta.strip(elelist[i])
            inta.strip()
    print(inta)
    return inta

stripper(inta)

def input_checker(intake):
        global nummol
        global numatom
        global numgram
        global nummlc
        global numvol
        if intake.count("mol") == 1 :
            intake.strip("mol")
            tpoi = "mol"
            nummol = intake
            intake.strip()
            return nummol
        elif intake.count("vol") == 1:
            intake.strip("vol")
            tpoi = "vol"
            numvol = intake
            intake.strip()
            return numvol
        elif intake.count("gram") == 1:
            intake.strip("gram")
            tpoi = "gram"
            numgram = intake
            intake.strip()
            return numgram
        elif intake.count("atom") == 1: 
            intake.strip("atom")
            tpoi = "atom"
            intake.strip()
            numatom = intake
            return numatom
        elif intake.count("mlc") == 1:
            intake.strip("mlc")
            tpoi = "mlc"
            intake.strip()
            nummlc = intake
            return nummlc
        else:
            print("Invalid input, Try again")
            exit()  

input_checker(elinum(inta))

def mmcalc(lis):
    global mm
    for i in range(0,len(lis)):
        mm += elementsgram[lis[i]]
    return mm    

mmcalc(eleininta)

def mainor(type):
    global nummol
    global numvol
    global nummlc
    global numatom
    global numgram
    if type == "gram":
        nummol = numgram/mm
        nummlc = nummol * na
        numatom = nummlc * len(eleininta)
        numvol = nummol * stp
    elif type == "mol":
        numgram = nummol * mm
        nummlc = nummol * na
        numatom = nummlc * len(eleininta)
        numvol = nummol * stp
    elif type == "mlc":
        nummol = nummlc/na
        numgram = nummol * mm
        numatom = nummlc * len(eleininta)
        numvol = nummol * stp
    print("mol = ", nummol)
    print("gram = ",numgram)
    print("mlc = ",nummlc)
    print("atom = ",numatom)
    print("vol = ",numvol)

print(tpoi)

mainor(tpoi)