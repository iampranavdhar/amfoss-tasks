testcases=int(input())
finalresult=[]
if testcases>1 and testcases<20:
    for i in range(testcases):
        N,M,K=input().split()
        mvalues1=list(map(int, input().split()))
        mvalues2=list(map(int, input().split()))
        sumofmvalues1=sum(mvalues1)
        sumofmvalues2=sum(mvalues2)
        mvalues2.sort(reverse=True)
        sumofklargestmvalues2=0
        if K>M:
            if sumofmvalues2>sumofmvalues1:
                a="YES"
                finalresult.append(a)
            elif sumofmvalues2<sumofmvalues1:
                b="NO"
                finalresult.append(b)
        elif K<M:
            for j in range(int(K)):
                sumofklargestmvalues2=sumofklargestmvalues2+mvalues2[j]
            if sumofklargestmvalues2>sumofmvalues1:
                c="YES"
                finalresult.append(c)
            elif sumofklargestmvalues2<sumofmvalues1:
                d="NO"
                finalresult.append(d)
    print(*finalresult,sep="\n")
else:
    quit



            



