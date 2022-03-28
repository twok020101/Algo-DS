from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        finalAns=[]
        noRows=len(mat)
        noCol=len(mat[0])
        for row in range (noRows):
            soldiers=0
            for col in range(noCol):
                if mat[row][col]==1:
                    soldiers+=1
            ans.append(soldiers)
        for i in range (k):
            x=min(ans)
            finalAns.append(ans.index(x))
            ans.remove(x)
        
        return finalAns

if __name__=="__main__":
    t=Solution()
    print(t.kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3))