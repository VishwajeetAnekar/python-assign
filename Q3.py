def print_primes(start, end):
    for num in range(start, end + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            print(num)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print_primes(start, end)
