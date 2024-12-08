# Given a list of numbers in random order write a linear time algorithm to find 
# the kth smallest number in the list. Explain why your algorithm is linear.
import random

# Background
SIZE = 1_000_000
RANDOM_RANGE = (-100_000_000_000, 100_000_000_000)
# Creating a random array
# Method 1
nums = [random.randint(*RANDOM_RANGE) for _ in range(SIZE)]
k = random.randrange(SIZE)

# Action
# To solve in linear time, we use Quickselect
# https://www.youtube.com/watch?v=XEmy13g1Qxc
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

_ = """
Average case of O(n) - assuming the choosing pivot is alwasy the middle element
Worst case of O(n^2) - pivot is always on either end of list. 
"""

def quick_select(left: int, right: int)-> int:
    pivot, p = nums[right], left
    
    for i in range(left, right):
        if nums[i] <= pivot:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1
        
    nums[p], nums[right] = nums[right], nums[p]
    
    if p > k:
        return quick_select(left, p-1)
    elif p < k:
        return quick_select(p+1, right)
    else:
        return nums[p]

print(f"k = {k} and kth smallest element: {quick_select(0, len(nums)-1)}")