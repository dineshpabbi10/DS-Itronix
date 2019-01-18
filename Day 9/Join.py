l=['chalk','duster','board','tablet','projector','pen']

for item in l:
    if item is not 'pen':
        print(item,"and ",end="")
    else:
        print(item)

print(" and ".join(l))
