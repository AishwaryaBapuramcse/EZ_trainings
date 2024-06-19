def divide(L,low,high):
    p=L[high]
    pi=high
    j=low-1
    for i in range(low,high):
        if L[i]<=p:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[pi]=L[pi],L[j]
    pi=j
    return pi
def Quick_sort(L,low,high):
    if low<high:
        pi=divide(L,low,high)
        print(pi,low,high)
        Quick_sort(L,low,pi-1)
        Quick_sort(L,pi+1,high)
    return
if __name__=="__main__":
    L=list(map(int,input().split()))
    low=0
    high=len(L)-1
    print(low,high)
    Quick_sort(L,low,high) 
    print("sorted array=",L)         

