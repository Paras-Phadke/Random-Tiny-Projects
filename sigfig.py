number = str(input("enter number = "))

def sigfigchecker(num):
    def deccheck(num):
        if num.count(".") == 1: 
            return True
        elif num.count(".") > 1:
            print("There is more than one decimal place,Try agian")
            exit()
        else:
            return False

    def digbdec(num):
        if deccheck(num):
            if num[0] == "0" and num[1] == ".":
                return True
        return False

    def firsigfig(num):
        place = 0
        if digbdec(num):
            for i in range(0,len(num)):
                if num[i] == "0" or num[i] == ".":
                    continue
                else:
                    place = i
                    break
        return place

    def nodec(num):
        place = 0
        for i in range(1,len(num)):
            if num[-i] == "0":
                continue
            else :
                place = i - 1
                break
        return place
    
    if digbdec(num):
        print("Number of significant figures is = ", len(num) - firsigfig(num))
        return len(num) - firsigfig(num)
    else:
        if deccheck(num):
            print("Number of significant figures is = ", len(num) - 1)
            return len(num) - 1
        else:
            print("Number of significant figures is = ",len(num) - nodec(num))
            return len(num) - nodec(num)

sigfigchecker(number)