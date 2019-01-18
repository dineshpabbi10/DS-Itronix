import bisect
n=5
a=[1,2,4,6,7,8,9,66]

print(bisect.bisect(a,n))
bisect.insort(a,n)
print(a)
