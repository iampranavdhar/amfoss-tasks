testcases=int(input())
finalresults=[]
for i in range(testcases):
    lists=[]
    n=long(input())
    for i in range(1,n):
        if i%3==0 or i%5==0:
            m=i
            lists.append(m)
    results=sum(lists)
    finalresults.append(results)
print(*finalresults,sep='\n')    


