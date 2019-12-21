import math

def palindrome(x):
    #if number is negative then it is not a palindrome
    if x <= 0:
        return x == 0
    #number of digits in the given integer
    num_digits = math.floor(math.log10(x))+1
    #most significant digit mask
    msd_mask = 10**(num_digits-1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:#if msd and lst are not equal then not palindrome
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True
    
print(palindrome(121))
