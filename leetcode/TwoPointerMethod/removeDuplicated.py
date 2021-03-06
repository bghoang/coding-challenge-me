'''
Given a sorted array nums, remove the duplicates in-place such that each element appear 
only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input 
array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2,
'''

'''
Optimal solution
Loop through the list of number nums
2 pointers, 2 cases can happen in this problem
First, 2 pointers point to the same value
    move the fast pointer 1 unit
Second, 2 pointer point to different value
    increase the slow pointer by 1, replace the value at slow pointer with
    the value at fast pointer
1 2 2 3 4 4
i
s

O(n) runtime
O(1) space complexity
'''


def removeDuplicates(nums):
    s = 0
    for i in range(len(nums)):
        if nums[i] != nums[s]:
            s += 1
            nums[s] = nums[i]

    return s+1
