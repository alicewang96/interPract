class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# working solution for: https://leetcode.com/problems/sum-of-left-leaves/
def sum_left_leaves(bn):		
	return sum_left_leaves(bn, 0)

def sum_left_leaves(bn, left_sum):
	if bn == None:
		return 0
	if bn.left == None and bn.right == None:
		# at a leaf node - return the sum we've created so far
		return left_sum
	tot_sum = 0
	if bn.left:
		# there exists a node on the left side
		if bn.left.left == None and bn.left.right == None:
			# bn.left is a left leaf node
			tot_sum += bn.left.val
		else:
			# bn.left is not a left leaf node, want to sum the left leaves in the
			# tree that has bn.left as its root
			tot_sum += sum_left_leaves(bn.left, left_sum)
	# need to add left leaves of the right tree
	tot_sum += sum_left_leaves(bn.right, left_sum)

	return tot_sum

''' 
description: 
given a string s, return the earliest index of a character that has a duplicate.

test cases:
given string "abba", return "a"
given string "abcbc", return "b"
'''
def earliest_duplicate(s):
	earliest_duplicate = len(s) + 1
	str_to_pos = {}
	for i in range(len(s)):
		c = s[i]
		if (c not in str_to_pos.keys()):
			str_to_pos[c] = i
		else:
			earliest_duplicate = min(earliest_duplicate, str_to_pos[c])
	if earliest_duplicate == len(s) + 1:
		return None
	return s[earliest_duplicate]

