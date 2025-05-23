#PRINT 5 TO 1 USING RECURSIVE FUNCTION
def show(n):
    if(n==0):      #base condition(condition at which recursion stops)
        return
    print(n)
    show(n-1)

show(5)