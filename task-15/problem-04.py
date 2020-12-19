testcases=int(input())
finalresults=[]
for i in range(testcases):
    max=-1
    N=int(input())
    for j in range(100,1000):
        for k in range(100,1000):
            num = str(k*j).split()[0]
            if len(num) == 6:
                if num[0]==num[-1] and num[1]==num[-2] and num[2]==num[-3] and int(num)<N and int(num)>max:
                    max=int(num)
    finalresults.append(max)
print(*finalresults,sep='\n')
