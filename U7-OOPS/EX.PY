str="vikas dange"

count=0
for i in range(0,len(str)):
    for j in range(i+1,len(str)-1):
        if str[i]!=str[j]:
            count+=1

print("Characters in largest substring are:",count)