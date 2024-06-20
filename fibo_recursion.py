def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
if __name__=="__main__":
    n=int(input())
    print(fib(n))


#the index u want the ans at is the input
#the fibo at that index is the output
#5--->input
#0 1 1 2 3
# last two numbers 2+3=5 is output at the 5th index