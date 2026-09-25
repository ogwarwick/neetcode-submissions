class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i1 in nums1:
            idx = nums2.index(i1)
            
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > i1:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)
        return result

