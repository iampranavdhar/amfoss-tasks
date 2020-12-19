testcases=int(input())
finalresults=[]
for i in range(testcases):
    lists=[1,2]
    finallist=[]
    n=int(input())
    for i in range(n):
        number=lists[i]+lists[i+1]
        if number>n:
            break
        else:
            lists.append(number)
    for i in range(len(lists)):
        if lists[i]%2==0:
            finallist.append(lists[i])
    summ=sum(finallist)
    finalresults.append(summ)
print(*finalresults,sep='\n')



