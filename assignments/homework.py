#Mahsa-Mehrbakhsh-first-exercise
def add():
    a1 = int(input("enter your number?".title()))
    b1 = int(input("enter your number?".title()))
    z1 = (a1 + b1)
    return (z1)
result = add()
print("result: ",result)

print("***") 

def add(a=2,b=3):
    z = (a+ b)
    return (z)
result = add()
print("result: " , result)

def add1(c=-1,d=1):
    x = (c + d)
    return(x)
result = add1()
print("result: ",result)

def add2(e=0,f=0):
    s = (e + f)
    return (s)
result = add2()
print("result: ",result)