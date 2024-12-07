# Previous Question-4
# Given a list of numbers in random order write a linear time algorithm to find the kth smallest number in the list. 
# Explain why your algorithm is linear.
# Present Question-5
# Can you improve the algorithm from the previous problem to be O(nlog(n))?
from random import shuffle, randrange

# Background
a_list = list(range(100_000))
shuffle(a_list)
k = randrange(100_000)

a_list.sort()
print(f"k = {k} and kth smallest element: {a_list[k]}")