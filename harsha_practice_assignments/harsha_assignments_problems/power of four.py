def isPowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 4 != 0):
            return False
        n = n // 4

    return True


# Driver code
test_no = 65
if (isPowerOfFour(65)):
    print(test_no, 'is a power of 4')
else:
    print(test_no, 'is not a power of 4')
