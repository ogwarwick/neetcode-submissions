class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != val:
                k += 1
            else:
                nums.pop(i)
        return k

        