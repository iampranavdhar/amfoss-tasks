testcases=int(input())
finalresults=[]

for i in range(testcases):
    factorsofn=[]
    N=int(input())
    maxx=-1
    for j in range(1,N+1):
        if N%j==0:
            factorsofn.append(j)
            
    for num in range(2,N+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                if num in factorsofn:
                    if num>maxx:
                        maxx=num
    finalresults.append(maxx)
print(*finalresults,sep='\n')

