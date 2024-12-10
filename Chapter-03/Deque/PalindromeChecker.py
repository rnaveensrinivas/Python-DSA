from Deque import Deque

def palindrome_checker(word: str) -> bool:
    d = Deque()
    for letter in word:
        d.add_rear(letter)
        
    while d.size() > 1:
        left = d.remove_front()
        right = d.remove_rear()
        if left != right:
            return False
    
    return True

print(palindrome_checker("madam"))
print(palindrome_checker("maddam"))
print(palindrome_checker("maddamaa"))
