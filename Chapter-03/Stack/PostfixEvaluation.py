from Stack import Stack

DIGITS = "0123456789"
def postfix_evaluation(postfix_exp: str) -> int:
    result = 0
    
    operand_stack = Stack()
    
    for token in postfix_exp:
        if token in DIGITS:
            operand_stack.push(int(token))
        elif token == " ":
            continue
        else:
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            
            resulting_operand = 0
            match token:
                case "^": resulting_operand = left_operand ** right_operand
                case "*": resulting_operand = left_operand * right_operand
                case "/": resulting_operand = left_operand // right_operand
                case "+": resulting_operand = left_operand + right_operand
                case "-": resulting_operand = left_operand - right_operand
            
            operand_stack.push(resulting_operand)
    
    return operand_stack.pop()

print(postfix_evaluation('7 8 + 3 2 + /'))
print(postfix_evaluation("2 3 + 7 5 - * 2 /")) # 5
print(postfix_evaluation("5342-^*")) # 45
