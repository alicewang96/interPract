# Invert binary tree: https://leetcode.com/problems/invert-binary-tree/
def invert(root):
	if root == None:
        return None
    elif root.right == None and root.left == None:
        return root
    else:
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
    return root

def moveZeroes(nums):
	
    # if len(nums) == 0:
    #     return None
    # if len(nums) == 1:
    #     return nums
    # if nums[0] == 0:
    #     return moveZeroes(nums[1:]) + nums[:1]
    # else:
    #     return nums[:1] + moveZeroes(nums[1:])

    earliest_zero = 0
    for cur < range(len(nums)):
    	if nums[cur] != 0:
    		nums[earliest_zero], nums[cur] = nums[cur], nums[earliest_zero]
    		earliest_zero += 1
    return nums

'''
sliding window algorithm with 3SUM:
given array arr, we want to find a pair of numbers that sum up to equal a value c

ex:
[-1, 0, 1, 2, -1, -4]
sorted:
[-4, -1, -1, 0, 1, 2]
i = -4, j = -1, k = 2 (negative of i)
-4 + -1 + 2 = -3
i = -4, j = -1, k = 2
-4 + -1 + 2 = -3
i = -4, j = 0, k = 2
-4 + 0 + 2 = -2
i = -4, j = 1, k = 2
-4 + 1 + 2 = -1
increment i 
i = -1, j = -1, k = 2
-1 + -1 + 2 = 0
solution: (-1, -1, 2)
'''




        