def print_num(n):
    if n<10:
        print(n)
        print_num(n+1)
        return
print_num(0)    