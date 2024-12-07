# Given a list of numbers in random order write a linear time algorithm to find the kth smallest number in the list. 
# Explain why your algorithm is linear.
from random import shuffle, randrange

# Background
a_list = list(range(100_000))
shuffle(a_list)
k = randrange(100_000)

# To solve in linear time, we use Quickselect

