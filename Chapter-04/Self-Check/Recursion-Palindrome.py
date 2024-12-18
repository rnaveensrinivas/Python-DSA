def preprocess(string: str) -> str:
    ret = []
    for s in string: 
        if s.isalnum(): 
            ret.append(s)
            
    return "".join(ret).lower()

def is_palindrome(string: str) -> bool:
    if len(string) == 1:
        return True
    if len(string) == 2:
        return string[0] == string[-1]
    
    return string[0] == string[-1] and is_palindrome(string[1:-1])

s = "Reviled did I live, said I, as evil I did deliver"
s = preprocess(s)
print(s)
print(is_palindrome(s))