from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=nums.count(val)
        for i in range (k):
            nums.remove(val)
        return k,nums

if __name__=="__main__":
    t=Solution()
    print(t.removeElement([0,1,2,2,3,0,4,2],2))