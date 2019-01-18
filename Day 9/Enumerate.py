a=['Karan Arora','T Series','Speed Records','White Hill Studios','Itronix Solutions']
i=0
for item in a:
    i=i+1
    if i%2==0:
        print(item)

print("\n<<<-----Using Enumerate----->>>")
for i,item in enumerate(a):
    print(i,item)

print("\n<<<-----Print Even Index Values Using Enumerate----->>>")
for i,item in enumerate(a):
    if(i+1)%2==0:
        print(item)
