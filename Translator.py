import math
Dec="0123456789"
Hex="0123456789ABCDEF"
Oct="01234567"
Bin="01"
def getD(j,k):
    n=0
    for i in range(len(j)):
       n+=int(k.find(str(j[len(j)-i-1])))*(pow(len(k),i))
    return(n)   #Return as Number

def setD(j,k):  
    l=int(j)
    n=""
    while(l>0):
       n=k[l%len(k)]+n
       l=math.floor(l/len(k))
    return(n)   #Return as String

print(setD("40",Bin))
print(getD("FF",Hex))
