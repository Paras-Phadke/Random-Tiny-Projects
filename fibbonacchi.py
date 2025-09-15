import pickle
import time
import time


global b
global temp
global datdict
global a

a = 0
b = 1
temp = 0

with open("C:\\Users\\nbpha\\OneDrive\\Desktop\\Python\\Rand\\fibodat.py" , "rb") as fi:
    datdict:dict = pickle.load(fi) 


datdict.update({1:a})
datdict.update({2:b})



term = int(input("Enter the number of terms: "))

start_time = time.time()

def useindex(term):
    try:
        print(datdict[term-1] + datdict[term - 2])
    except: genfibo(term)

def genfibo(terms):
    a = 0
    b = 1
    temp = 0
    for i in range(0,terms):
        temp = a + b
        a = b
        b = temp
        datdict.update({i+3:temp})
    
    print(temp)

print(datdict)

with open("C:\\Users\\nbpha\\OneDrive\\Desktop\\Python\\Rand\\fibodat.py" , "wb") as fi:
    pickle.dump(datdict,fi)


print("--- %s seconds ---" % (time.time() - start_time))