conversion = False
inhexnum = ""
inhexlis = []
inoctnum = ""
inbinnum = ""
decres = 0

hexlook = {
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    }

invhexlook ={
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F",
    
}

inbas = input("Enter the base: ")
inbase = inbas.lower()
inbase.replace(" ","")
inbase.replace("0","")

if inbase == "dec" or inbase == "decimal":
    decres = int(input("Enter Decimal number: "))
elif inbase == "hex" or inbase == "hexadecimal":
    inhexnum = input("Enter Hex number: ")
    inhexlis = list(inhexnum)
    for i in range(0,len(inhexlis)):
        decres += hexlook[inhexlis[len(inhexlis) - i - 1]] * (16 ** i)
elif inbase == "oct" or inbase == "octal":
    inoctnum = input("Enter Octal number: ")
    for i in range(0,len(inoctnum)):
        decres += int(inoctnum[len(inoctnum) - i - 1]) * (8 ** i)
elif inbase == "bin" or inbase == "binary":
    inbinnum = input("Enter Binary number: ")
    for i in range(0,len(inbinnum)):
        decres += int(inbinnum[len(inbinnum) - i - 1]) * (2 ** i)


def dectohex(num):
    hexres = "" 
    rem = num % 16
    quo = num // 16
    hexres = "".join([invhexlook[rem],hexres])
    while True:
        if quo < 16:
            hexres = "".join([invhexlook[quo],hexres])
            break
    
        while quo >= 16:    
            rem = quo % 16
            hexres = "".join([invhexlook[rem],hexres])
            quo //= 16
    return hexres

def dectooct(num):
    octres = ""
    rem = int(num % 8)
    quo = int(num // 8)
    octres = "".join([str(rem),octres])
    while True:
        if quo < 8:
            octres = "".join([str(quo),octres])
            break
        while quo >= 8:
            rem = quo % 8
            octres = "".join([str(rem),octres])
            quo //= 8
    return octres

def dectobin(num):
    binres = ""
    rem = int(num % 2)
    quo = int(num // 2)
    binres = "".join([str(rem),binres])
    while True:
        if quo < 2:
            binres = "".join([str(quo),binres])
            break
        while quo >= 2:
            rem = quo % 2
            binres = "".join([str(rem),binres])
            quo //= 2
    return binres

if True:
    print("################ RESULTS ################")
    print("   Decimal form is: ",decres)
    print("   Hexadecimal form is: ",dectohex(decres))
    print("   Octal form is: ",dectooct(decres))
    print("   Decimal from is: ",dectobin(decres))