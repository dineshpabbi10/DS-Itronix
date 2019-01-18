users=['Karan','Prakash','Arpit','Varun','Sahil']
computer=['Raspberry Pi','Android','Iphone','Beagle Bone','Intel Gallilio']

for i in range(0,len(users)):
    print("Computer used by",users[i],"is",computer[i])

print("\n<<<------Using Format------>>>")
for i in range(0,len(users)):
    a="Computer used by {} is {}".format(users[i],computer[i])
    print(a)

print("\n<<<------Change Order Using Format------>>>")
for i in range(0,len(users)):
    a="Computer used by {1} is {0}".format(users[i],computer[i])
    print(a)

