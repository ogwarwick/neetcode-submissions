class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = res = 0
        for i in nums:
            if i == 1:
                current_count += 1
            else:
                current_count = 0
            res = max(res, current_count)
        return res




