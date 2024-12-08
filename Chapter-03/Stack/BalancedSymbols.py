from Stack import Stack

def is_matching(opening: str, closing: str) -> bool:
    openings = "([{"
    closings = ")]}"
    return openings.index(opening) == closings.index(closing)

def symbols_checker(symbol_string: str) -> bool:
    s = Stack()
    
    for symbol in symbol_string:
        if symbol in {"(", "{", "["}:
            s.push(symbol)
        elif symbol in {")", "}", "]"}:
            if s.is_empty():
                return False
            popped = s.pop()
            # if not (ord(popped) == ord(symbol) - 2 or
            #         ord(popped) == ord(symbol) - 1):
            #     return False
            if not is_matching(popped, symbol):
                return False
                
    return s.is_empty()

test_cases = ['(()', '((()))', "( [ ) ]" , 
              " ( ( ( ) ] ) )", " [ { ( ) ]", 
              " { { ( [ ] [ ] ) } ( ) }", 
              " [ [ { { ( ( ) ) } } ] ]", 
              " [ ] [ ] [ ] ( ) { }"]

for test_case in test_cases:
    print(symbols_checker(test_case))