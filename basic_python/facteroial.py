#recursion means calling the function itself directly or indirectly
def facteroial(n):
    if(n<2):
        return 1
    return n*facteroial(n-1)
print("factorial of 3:",facteroial(3))
print("factorial of 5:",facteroial(5))
print("factorial of 10:",facteroial(10))
print("factorial of 20:",facteroial(20))



