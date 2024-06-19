n=int(input("enter the num of elements"))
lst=list(map(int,input("enter the elements : ").split()))
for j in range(0,n):
    pos=j
    min=lst[j]
    for i in range(j,n):
        if lst[i]<min:
            min=lst[i]
            pos=i
            lst[j],lst[pos]=lst[pos],lst[j]    
print(lst)        