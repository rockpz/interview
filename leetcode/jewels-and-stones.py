class Solution():
	"""
	You're given strings J representing the types of stones that are jewels, 
	and S representing the stones you have.  Each character in S is a type of stone you have.  
	You want to know how many of the stones you have are also jewels.

	The letters in J are guaranteed distinct, and all characters in J and S are letters. 
	Letters are case sensitive, so "a" is considered a different type of stone from "A".
	"""
	def num_jewels_in_stones(self, jewels, stones):
		count = 0
		for stone in stones:
			if stone in jewels:
				count = count + 1
		return count


if __name__ == '__main__':
	jewels = 'aA'
	stones = 'aAABBBB'
	Solution().num_jewels_in_stones(jewels, stones)
