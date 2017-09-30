b=[]
def prm(a,n):
    if(n==0):
        j=0
        for i in a:
            if(a.count(i)!=b.count(i)):
                j=1
        if(j==0):
            print(b)
        return
    else:
        for i in a:
            b.append(i)
            prm(a,n-1)
            b.pop()
        

a=input()
prm(a,len(a))
