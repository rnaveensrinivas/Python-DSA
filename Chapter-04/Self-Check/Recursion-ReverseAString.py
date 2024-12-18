def reverse_a_string(s: str) -> str:
    if len(s) == 1:
        return s
    else:
        return reverse_a_string(s[1:]) + s[0]

print(reverse_a_string("neevaN"))