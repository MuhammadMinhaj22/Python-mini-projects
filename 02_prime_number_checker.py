n = int(input("Enter a number to check if it's prime: "))
if n > 1:
    for i in range(2, n):
        if(n % i)==0:
            print(f"{n} is not a prime number.")
            print(f"It is divisible by {i}.")
            break
    else:
        print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
