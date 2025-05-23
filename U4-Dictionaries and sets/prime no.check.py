n = int(input("Enter the number to check whether it is prime:"))
flag = False
for i in range(2,n):
    if (n % i ==0):
        flag = True
        break

if flag:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")

