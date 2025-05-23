#using for loop
n=int(input("Enter number n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i

print("sum of n nos. is:",sum)

#using while loop
n=int(input("Enter number n:"))
sum=0
i=0
while i<=n :
    sum=sum+i
    i+=1

print("sum of n nos. is:",sum)