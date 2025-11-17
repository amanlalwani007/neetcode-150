class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =[]
        for  i in range(len(nums)-2):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            val = nums[i]
            left = i+1
            right = len(nums)-1
            while left< right:
                if val + nums[left] + nums[right] == 0 :
                    ans.append([val , nums[left], nums[right]])
                    left+=1
                    while left<right and  nums[left] == nums[left-1]:
                        left+=1
                elif nums[left] + nums[right] < -val:
                    left+=1
                else:
                    right-=1
        return ans


# time complexity :- O(n**2)
# space complexity :- O(1)            


        