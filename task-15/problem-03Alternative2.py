testcases=int(input())
finalresults=[]

def intersection(lst1,lst2):
    lst3=[value for value in lst1 if value in lst2]
    return max(lst3)

for i in range(testcases):
    primenumbers=[]
    factorsofn=[]
    N=int(input())
    for num in range(2,N+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                primenumbers.append(num)
    for j in range(1,N+1):
        if N%j==0:
            factorsofn.append(j)
    finalresults.append(intersection(primenumbers,factorsofn))
print(*finalresults,sep='\n')
