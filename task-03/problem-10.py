testcases=int(input())
finalresults=[]

for i in range(testcases):
    N,K=map(int,input().split())
    N_as_string=str(N)
    No_Of_ninja_possible=len(N_as_string)-K+1
    ninja_sum_list=[]
    min_ninja=[]

    for j in range(No_Of_ninja_possible):
        ninjasum=0
        for k in range(K):
            ninjasum += int(N_as_string[j+k])
        ninja_sum_list.append(ninjasum)

    for l in range(len(ninja_sum_list)-1):
        m=abs(ninja_sum_list[l] - ninja_sum_list[l+1])
        min_ninja.append(m)

    if not min_ninja:
        n='-1'
        finalresults.append(n)

    else:
        finalresults.append(min(min_ninja))
print(*finalresults,sep='\n') 


