from Stack import Stack

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decimal_to_base(num: int, base:int ) -> str:
    
    remainder_stack = Stack()
    
    while num: 
        remainder_stack.push(num % base)
        num //= base
    
    ret = ""
    while not remainder_stack.is_empty():
        ret += DIGITS[remainder_stack.pop()]
        
    return ret

print(decimal_to_base(25, 2)) # 25
print(decimal_to_base(25, 16)) # 19

# Self-check
# 1. What is the value of 25 expressed as an octal number?
print(decimal_to_base(25, 9)) # 27
# 2. What is the value of 256 expressed as a hexidecimal number?
print(decimal_to_base(256, 16)) # 100
# 3. What is the value of 26 expressed in base 26?
print(decimal_to_base(26, 26)) # 10


    