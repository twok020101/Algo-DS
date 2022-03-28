from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1,nums2=set(nums1),set(nums2)
        commonNumber=nums1.intersection(nums2)
        for x in commonNumber:
            nums1.remove(x)
            nums2.remove(x)
        return [list(nums1),list(nums2)]

if __name__=="__main__":
    t=Solution()
    print(t.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))