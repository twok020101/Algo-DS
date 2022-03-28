from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half=((intLength-1)//2)-1
        print("half=",half)

        def get(x):
            x-=1
            print("x=",x)
            r=(10**half)+x
            print("r int=",r)
            s=str(r)
            if intLength%2==0:
                print("s add even = ",s+s[::-1])
                return s+s[::-1]
            else:
                print("s odd = ",s+s[::-1][1:])
                return s+s[::-1][1:]

        ans=[]
        for q in queries:
            r=get(q)
            print("r=",r)
            if len(r)!=intLength:
                r="-1"
                ans.append(int(r))
        return ans

if __name__=="__main__":
    t=Solution()
    print(t.kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3))