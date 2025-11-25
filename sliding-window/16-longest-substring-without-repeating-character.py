# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right =0 
        longest = 0
        mapper = {}
        while right < len(s):
            if s[right] in mapper:
                left = max(left, mapper[s[right]] + 1)
            mapper[s[right]] = right
            longest = max(longest, right - left + 1)
            right += 1
        return longest


# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution :- Sliding Window , we use a hashmap to store the last index of the character, and if the character is already in the hashmap, we update the left pointer to the next index of the character.