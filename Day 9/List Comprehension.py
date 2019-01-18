l=[1,3,4,5,6,7,8,9,13,23,4,39,57,356,4,667,5,43,76,74,34]
divide_by_3=[]
for item in l:
    if item%3==0:
        divide_by_3.append(item)


print('Without List Comprehensions',divide_by_3)
print('With List Comprehensions',[item for item in l if item%3==0])

print("\n<<<-----Generator----->>>")
gen=(i for i in range(56) if i%3==0)
print(gen) #Object Create : Save memory, But it will take time to run
for item in gen:
    print(item,end=" ")

print()
squared={x**2 for x in [1,2,3,4,4,4,4,3,3,2,2,1]}
print(squared)




