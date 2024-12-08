from Stack import Stack

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
PRECEDENCE = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
}

def infix_to_postfix(infix_exp: str) -> str:
    
    postfix = ""
    
    operator_stack = Stack()
    
    for token in infix_exp:
        if token in LETTERS or token in NUMBERS:
            postfix += token
            continue
        
        if token == " ":
            continue
        
        if token == "(":
            operator_stack.push(token)
        elif token == ")":
            while operator_stack.peek() != "(":
                postfix += operator_stack.pop()
            operator_stack.pop() # discard '('
        else:
            # operator
            if operator_stack.is_empty():
                operator_stack.push(token)
            else:
                while (not operator_stack.is_empty() and
                       PRECEDENCE[operator_stack.peek()] >= PRECEDENCE[token]):
                    postfix += operator_stack.pop()
                operator_stack.push(token)    
    
    while not operator_stack.is_empty():
        postfix += operator_stack.pop()
        
    return postfix

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C- ( D- E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
print(infix_to_postfix("A + B * C"))
print(infix_to_postfix("10 + 3 * 5 / (16 - 4)"))
print(infix_to_postfix("5 * 3^(4 -2)"))
