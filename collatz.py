""" verifying collatz conjecture. """

# Stephen Welch 
def f(n):
    # if n is even
    if n % 2 == 0:
        return n // 2
    # if n is odd
    elif n % 2 == 1:
        return (3 * n) + 1
    else:
        return None

def collatz(n):
    # Puts in into a list
    so_far = []
    # Loop until n is 1
    while n != 1:
        if n in so_far:
            return False 
        so_far.append(n)
        n = f(n)
    so_far.append(n)
    return so_far
#print(collatz(10))
print(collatz(27))
