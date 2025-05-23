#WRITE A RECURSIVE FUNCTION TO CALCULATE SUM OF FIRST N NATURAL NUMBERS
def sum(n):
    if(n==0) :
        return 0
    else:
        return n+sum(n-1)        #RECURSION IS USED
    
print(sum(50))