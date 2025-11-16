class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hash_set:
                length = 1
                while (num + length) in hash_set:
                    length += 1
                longest = max(longest, length)
        return longest




# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

# optimal approach: we use a hashset to store the elements of the array
# we iterate through the array and check if the current element is the start of a consecutive sequence
# if it is, we check if the next element is in the array and if it is, we increment the count
# if it is not, we break the loop
# we return the max count
# time complexity: O(n) - we iterate through the array once and check if the current element is the start of a consecutive sequence
# space complexity: O(n) - we store the hashset
# leetcode: https://leetcode.com/problems/longest-consecutive-sequence/
