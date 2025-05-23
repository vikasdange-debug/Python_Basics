#WAF TO FIND THE FACTORIAL OF NUMBER
def calc_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print("factorial is:",factorial)

calc_factorial(5)