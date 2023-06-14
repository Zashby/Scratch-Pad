# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i, x in enumerate(nums)]

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  
        for i , x in enumerate(nums):
            
            if sum(nums[0:i])==sum(nums[i+1:len(nums)]):
                return i
        return -1

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = [s.index(x) for x in s]
        t_map = [t.index(y) for y in t]
        return s_map == t_map
        
 