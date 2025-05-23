list=[1,2,3,2,1]
list2=list.copy()
list2.reverse()
if(list2==list):
    print("list is a palindrome")
else:
    print("list is not a palindrome")