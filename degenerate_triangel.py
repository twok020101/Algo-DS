def check(a,b,c):
    if a<b+c and b<b+c and c<c+a:
        return True
    return False

if __name__=="__main__":
    a,b,c=[],[],[]
    for i in range (int(input())):
        a.append(int(input()))
    for j in range (int(input())):
        b.append(int(input()))
    for k in range (int(input())):
        c.append(int(input()))
    for z in range(len(a)):
        if check(a[z],b[z],c[z]):
            print("Yes")
        else:
            print("No")
         
