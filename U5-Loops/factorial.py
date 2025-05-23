#Using for loop
n=int(input("Enter number n:"))
i=1
fact=1
for i in range(1,n+1):
    fact=fact*i
    
print("factorial is :",fact)

#using while loop
n=int(input("Enter number n:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1

print("factorial is :",fact)