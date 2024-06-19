n=int(input("enter the num of elements"))
lst=list(map(int,input("enter the elements : ").split()))
for j in range(0,n):
    for el in range(0,n-1-j):
        if lst[el]>lst[el+1]:
            lst[el],lst[el+1]=lst[el+1],lst[el]
        else:
            pass
print(lst)        