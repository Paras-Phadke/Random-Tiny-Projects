firsname = input("input the first name: ").lower()
secsname = input("input the second name: ").lower()

firname = list(firsname.replace(" ",""))
secname = list(secsname.replace(" ",""))

for letr in firname:
    if letr in secname:
        firname.remove(letr)
        secname.remove(letr)

res = len(firname) + len(secname)

if res % 6 == 0:
    print("S")
elif res % 6 == 1:
    print("F")
elif res % 6 == 2:
    print("L")
elif res % 6 == 3:
    print("A")
elif res % 6 == 4:
    print("M")
else:
    print("E")
