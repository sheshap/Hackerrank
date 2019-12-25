#count bits
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x&1 
        x>>=1 
    return num_bits

print(count_bits(23))

#check parity
def paritycheck(x):
    parity = 0
    while x:
        parity^=x&1 
        x>>=1 
    return parity
    
print(paritycheck(31))

#swap bits 
def bit_swap(x,i,j):
    if (x>>i) & 1 != (x>>j) & 1:
        bit_mask = (1<<i)|(1<<j)
        x^=bit_mask
    return x 
    
print(bit_swap(23,1,2))
print(bit_swap(23,2,3))
