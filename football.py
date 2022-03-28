def score(a,b):
    ans=[]
    for x in b:
        count=0
        for y in a:
            if y<=x:
                count+=1
        ans.append(count)
    return ans

if __name__=="__main__":
    a=[]
    b=[]
    for i in range (int(input())):
        a.append(int(input()))
    for j in range(int(input())):
        b.append(int(input()))
    ans=score(a,b)
    for x in ans:
        print(x)