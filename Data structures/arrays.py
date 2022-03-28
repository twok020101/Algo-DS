class Array:
    def __init__(self,arr) -> None:
        self.arr=arr
    
    #---------------------------------------SORTING--------------------------------------------------#
    
    #Bubble sort
    def bubbleSort(self):
        tempArr=self.arr
        N=len(tempArr)
        for iter_num in range(N-1,0,-1):
            for idx in range (iter_num):
                if tempArr[idx]>tempArr[idx+1]:
                    temp=tempArr[idx]
                    tempArr[idx]=tempArr[idx+1]
                    tempArr[idx+1]=temp

        return tempArr

    #Merge Sort 
    def mergerSort(self):

        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            
            mid=len(arr)//2
            leftList=arr[:mid]
            rightList=arr[mid:]

            leftList=merge_sort(leftList)
            rightList=merge_sort(rightList)
            return merge(leftList,rightList)
        
        def merge(leftList,rightList):
            res=[]
            while len(leftList)!=0 and len(rightList)!=0:
                if leftList[0]<rightList[0]:
                    res.append(leftList[0])
                    leftList.remove(leftList[0])
                else:
                    res.append(rightList[0])
                    rightList.remove(rightList[0])
                
            if len(leftList)==0:
                res+=rightList
            else:
                res+=leftList

            return res

        tempArr1=self.arr
        return merge_sort(tempArr1)
    
    #Insertion Sort
    def insertionSort(self):
        tempArr=self.arr
        for step in range (1,len(tempArr)):
            key=tempArr[step]
            j=step-1

            while j>=0 and key<tempArr[j]:
                tempArr[j+1]=tempArr[j]
                j-=1

            tempArr[j+1]=key
        return tempArr

if __name__=="__main__":
    arr=[65,35,98,41,37,64,0,2,9,5,12,3657]
    t=Array(arr)
    # print(t.bubbleSort())
    # print(t.mergerSort())
    print(t.insertionSort())