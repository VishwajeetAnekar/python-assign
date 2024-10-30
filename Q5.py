n = 10

for i in range(n):
    print(" " * i, end="")
    if i % 2 == 0:
        print("* " * (n - i))
    else:
        print("# " * (n - i))