class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = []
            hash_map[sorted_str].append(str)
        return list(hash_map.values())

# time complexity: O(n * k log k) - we iterate through the strings once and sort each string
# space complexity: O(n * k) - we use a hashmap to store the sorted strings and the original strings 