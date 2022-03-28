from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        N=len(nums)
        count=0
        for i in range(N):
            if (i+count)%2==0:
                if i+1<N and nums[i]==nums[i+1]:
                    count+=1

        if (N-count)%2==1:
            count+=1

        return count

if __name__=="__main__":
    t=Solution()
    print(t.minDeletion(nums = [1,1,2,3,5]))
    print(t.minDeletion(nums = [1,1,2,2,3,3]))

#[0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5]
#                                        