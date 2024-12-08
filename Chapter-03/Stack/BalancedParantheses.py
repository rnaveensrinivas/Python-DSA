from Stack import Stack

def parantheses_checker(symbol_string: str) -> bool:
    s = Stack()
    
    for symbol in symbol_string:
        if symbol == "(":
            s.push('(')
        elif symbol == ")":
            if s.is_empty():
                return False
            s.pop()
    
    return s.is_empty()

print(parantheses_checker('((()))'))
print(parantheses_checker('(()'))