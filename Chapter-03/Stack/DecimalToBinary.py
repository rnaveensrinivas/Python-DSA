from Stack import Stack

def decimal_to_binary(num: int) -> str:
    s = Stack()
    
    while num: 
        s.push(num%2)
        num //= 2
    
    ret = ""
    while not s.is_empty():
        ret += str(s.pop())
        
    return ret

print(decimal_to_binary(42))