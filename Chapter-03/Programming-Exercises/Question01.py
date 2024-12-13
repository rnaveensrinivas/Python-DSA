# Question 1. Modify the infix-to-postfix algorithm so that it can 
# handle errors.

# redefining stack - for sake of practice
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)

    def push(self, item: object) -> None:
        self.items.append(item)
        
    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
PRECEDENCE = {
    "^": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 1,
}
def infix_to_postfix(infix_string: str) -> str:
    
    postfix_list = []
    op_stack = Stack()
    
    i = 0
    while i < len(infix_string):
        
        if (infix_string[i] in LETTERS or infix_string[i] in NUMBERS):
            postfix_list.append(infix_string[i])
        elif infix_string[i] == "(":
            op_stack.push("(")
        elif infix_string[i] == ")":
            
            while op_stack.peek() != "(":
                postfix_list.append(op_stack.pop())
            op_stack.pop() # removing "("
            
            
        elif infix_string[i] in PRECEDENCE:
            while (not op_stack.is_empty() and
                   PRECEDENCE[op_stack.peek()] >= PRECEDENCE[infix_string[i]]):
                postfix_list.append(op_stack.pop())
                
            op_stack.push(infix_string[i])
            
        i += 1      
    
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return "".join(postfix_list)


TEST_CASES = [
    ("a + b + 10 + 23", "ab+10+23+"),
    ("a + b * 10 + 23", "ab10*+23+"),
    ("(a + b) * (10 + 23)", "ab+1023+*"),
    ("a", "a"),
    ("((a + b) * c) + d", "ab+c*d+"),
    ("a * b + c / d - e", "ab*cd/+e-"),
    ("a - b + c", "ab-c+"),
    ("(a + b) * c - (d + e) / f", "ab+c*de+f/-"),
    ("a + b * c ^ d", "abcd^*+"),
    ("a * (b + c * d) - e / f ^ g + h", "abcd*+*efg^/-h+")
]

# Running test cases
for expression, expected in TEST_CASES:
    result = infix_to_postfix(expression)
    print(f"Result: {"Pass" if result == expected else "Fail"} "
          f"{expression} => {result} (Expected: {expected})")
