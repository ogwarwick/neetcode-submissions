class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums:
                diff_index = nums.index(diff)
                if index != diff_index:
                    return [min(index, diff_index), max(index, diff_index)]


            




        
            
        