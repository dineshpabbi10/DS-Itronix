#map(function,list)

l=[1,2,3,5,6,7]
sq=[]
for item in l:
    sq.append(item**2)
print(sq)

print("\n<<<-----Using MAP Function----->>>")

def square(n):
    return n**2

l1=[1,2,3,5,6,7]
sq1=[]
sq1=list(map(square,l1))
print(sq1)

print("\n\n<<<-----Filter in Python----->>>")
def greater(n):
    if n>2:
        return True
    else:
        return False
l2=[1,2,3,4,5,6,7,-3,-44,-54]
greater_then_2=list(filter(greater,l2))
print(greater_then_2)

#Values which return True will append in list

print("\n\n<<<-----Reduce in Python----->>>")
from functools import reduce

def sum(a,b):
    return a+b

l=reduce(sum,[1,2,4,6,7])
print(l)
#Reduce function first add 1+2=3 then 3+4=7......








