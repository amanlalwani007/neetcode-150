from queue import PriorityQueue
class Solution:
    # hashmap + priority Queue 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        priority_queue = PriorityQueue()
        for num, count in hash_map.items():
            # storing -count to get the highest frequent elements cause priority queue is a min heap
            priority_queue.put((-count, num))
        result= []
        for _ in range(k):
            result.append(priority_queue.get()[1])
        return result



# Approach 1 
# hashmap + sort = Time complexity: O(n log n)

# Approach 2
# hashmap + priority queue = Time complexity: O(n log k)

# Approach 3
# hashmap + heap = Time complexity: O(n log k)


