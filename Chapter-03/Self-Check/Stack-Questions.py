import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
_ = """
os.path.dirname(__file__) gets the directory of the current script.
os.path.join(..., '..') moves up to the parent directory.
os.path.abspath(...) makes the path absolute.
sys.path.append() we are appending to system's path
"""
# Now you can import the file
from Stack import Stack

m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
print(m.peek())
print("---- ---- ----")
# ---- ---- ----

# m = Stack()
# m.push('x')
# m.push('y')
# m.push('z')
# while not m.is_empty():
#     m.pop()
#     m.pop()
    
# print("---- ---- ----")
# ---- ---- ----

def rev_string(my_string: str) -> str:
    s = Stack()
    for c in my_string:
        s.push(c)
    
    ret = ""
    while not s.is_empty():
        ret += s.pop()
    
    return ret

name = "Naveen"
print(rev_string(name))