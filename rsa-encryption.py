import random

def lcm(x,y): # least common multiple function
    greater = x
    if x > y:
        greater = x
    else:
        greater = y
    
    while((greater % x != 0) or (greater%y != 0)):
        greater+=1
    return greater
    
def gcd(x,y): # greatest common divisor
    if x < y:
        temp = x
    else:
        temp = y
    while ((x%temp != 0) or (y%temp != 0)):
        temp-=1
    return temp

def prime():
    while(True):
        x=random.randint(1,10**3)
        sqrt=int(x**0.5)+1
        for i in range(2,sqrt+1,1):
            if (x%i != 0):
                if (sqrt == i):
                    return x
            else:
                break

def process(msg,n,key):
    return (msg**key) % n
p=prime()
q=prime()
print("(p,q)=("+str(p)+","+str(q)+")")

n = p*q
l = lcm(p-1,q-1)

for e in range(2,l,1):
    if gcd(e,l) == 1:
        break

for d in range(2,l,1):
    if (e*d)%l == 1:
        break


#print(p, q, l, e, d)
print("Public key:",e)
print("Private key:",d)

msg="Hello, world" #plain text
index=[]
for i in range(len(msg)):
    index.append(ord(msg[i]))
temp=0
while(True):
    if msg[temp] == chr(process(process(index[temp],n,e),n,d)):
        temp+=1
        if temp == len(msg)-1:
            print("success")
            break
    else:
        print("wasted")
        break
    
    