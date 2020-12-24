testcases=int(input())
finalresults=[]
for i in range(testcases):
    number=[]
    n=int(input())
    lists=[1,2,3]
    if n==1 or n==2 or n==3:
        number.append(n)
    elif n>3:
        for i in range(0,(n-3)):
            nxtnum=lists[i]+lists[i+1]+lists[i+2]
            lists.append(nxtnum)
        number.append(max(lists))
    for i in range(len(number)):
        numm=number[i]
        m=int(numm%(10**9 + 7))
        revnum = 0
        while(m > 0): 
            a = m % 10
            revnum = revnum * 10 + a 
            m = m // 10
        finalresults.append(revnum)
print(*finalresults,sep='\n')






