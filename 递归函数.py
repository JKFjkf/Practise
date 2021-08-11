def factorial_normal(n):
    result = 1
    for i in range(n):
        result = result * n
        n = n-1
    return result

def factorial_recursion(n):
    if n == 1:
        return 1
    return n *factorial_recursion(n-1)

if __name__ == '__main__':
    n=5
    print(factorial_recursion(n))
    print(factorial_normal(n))