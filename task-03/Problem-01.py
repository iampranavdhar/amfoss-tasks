sums=[]
testcases=int(input())
for i in range(testcases):
    k = int(input())
    str = input() 
    count = 0
    res = "" 
    for ele in str: 
        if ele == ' ': 
            count = count + 1
            if count == k+1: 
                break
            res = "" 
        else : 
            res = res + ele
    sum=0
    if count >= k:
        for j in range(len(res)):
            sum=sum+ord(res[j])
        sums.append(sum)
    elif count < k:
        m='-1'
        sums.append(m)
print(*sums,sep="\n")