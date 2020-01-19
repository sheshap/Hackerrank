#function to check if a string is a palindrome
def is_palindrome(s): 
    return all(s[i]==s[~i] for i in range(len(s)//2))
    
#function to convert an integer to string
def int_to_string(x):
    is_negative = False
    if x<0:
        x, is_negative = -x, True
    s = []
    while True: #chr() method returns a character whose unicode point is num, an integer.
        s.append(chr(ord('0') + x % 10)) #ord() returns value of the byte when the argument is an 8-bit string
        x //= 10
        if x == 0:
            break
    #reversed() process the items in a sequence in reverse order
    return ('-' if is_negative else '')+''.join(reversed(s))
    
