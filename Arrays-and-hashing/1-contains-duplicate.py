class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = {}
        for num in nums:
            if num in hash_set:
                return True
            hash_set[num] = True
        return False




#Time Complexity: O(n)
#Space Complexity: O(n)








