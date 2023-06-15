print("Enter M")
m=int(input())
print("Enter N")
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(int(input()))
for k in range(len(a)):
    if a[k] + min(a) <= m:
        b += [[a[k], min(a)]]
        a[k] += m
        a[a.index(min(a))] += m
    else:
        if a[k] > m:
            continue
        else:
            b += [[a[k]]]
print(len(b))




