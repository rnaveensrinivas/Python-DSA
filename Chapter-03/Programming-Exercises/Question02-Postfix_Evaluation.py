#  2. Modify the postfix evaluation algorithm so that it can handle errors.
class Stack:
    def __init__(self):
        self.items = []
        
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return self.size() == 0
        
    def push(self, item: object) -> None:
        self.items.append(item)
    
    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Cannot pop() from empty stack")
        return self.items.pop()
    
    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Cannot peek() from empty stack")
        return self.peek[-1]
    
    def __str__(self) -> str:
        return f"Base -> {self.items} <- Top"

NUMBERS = "1234567890"
OPERATORS = "^+-/*"
def postfix_evaluation(postfix: str) -> int:
    operand_stack = Stack()
    for token in postfix: 
        if token in NUMBERS:
            operand_stack.push(int(token))
        elif token == " ":
            continue
        elif token in OPERATORS:
            try: 
                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()
            except: 
                raise ValueError("Postfix expression is invalid.")
            match token:
                case '^': operand_stack.push(left_operand**right_operand)
                case '*': operand_stack.push(left_operand*right_operand)
                case '/': operand_stack.push(left_operand//right_operand)
                case '+': operand_stack.push(left_operand+right_operand)
                case '-': operand_stack.push(left_operand-right_operand)
        else:
            raise ValueError("Postfix expression is invalid")
    
    try:
        ret = operand_stack.pop()
    except: 
        raise ValueError("Postfix expression is invalid")
    
    if not operand_stack.is_empty():
        raise ValueError("Postfix expression is invalid")
    
    return ret

# Valid test cases
print(postfix_evaluation("34+"))                        # 7
print(postfix_evaluation("7 8 + 3 2 + /"))              # 3
print(postfix_evaluation("2 3 + 7 5 - * 2 /"))          # 5
print(postfix_evaluation("5342-^*"))                    # 45
print(postfix_evaluation("5 1 2 + 4 * + 3 -"))          # 14
print(postfix_evaluation("8 2 / 3 -"))                  # 1
print(postfix_evaluation("2 3 + 4 5 * +"))              # 25
print(postfix_evaluation("3 5 8 * 7 + *"))              # 141
print(postfix_evaluation("6 2 / 3 + 4 2 * +"))          # 15
print(postfix_evaluation("4 5 + 2 3 ^ +"))              # 13
print(postfix_evaluation("3 4 5 * 6 - *"))              # -66
print(postfix_evaluation("2 3 ^ 4 ^"))                  # 4096
print(postfix_evaluation("8 3 2 * + 4 5 + *"))          # 88
print(postfix_evaluation("7 8 3 2 + + *"))              # 91
print(postfix_evaluation("5 1 2 3 * + +"))              # 12
print(postfix_evaluation("6 2 / 4 2 ^ +"))              # 10
print(postfix_evaluation("6 2 5 * - 3 +"))              # -7
print(postfix_evaluation("4 2 ^ 3 3 ^ +"))              # 31
print(postfix_evaluation("7 3 * 2 1 + /"))              # 10
print(postfix_evaluation("8 3 2 + * 4 /"))              # 10
print(postfix_evaluation("3 3 ^ 3 2 * +"))              # 36
print(postfix_evaluation("4 2 ^ 3 + 2 ^"))              # 169
print(postfix_evaluation("5 1 2 + 4 * + 3 -"))          # 14
print(postfix_evaluation("3 4 + 5 * 2 -"))              # 33
print(postfix_evaluation("6 2 3 ^ * 4 /"))              # 36
