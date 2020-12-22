testcases = int(input())
finalresults=[]
for i in range(testcases):
    N,K = input().split()
    amount = list(map(int, input().split()))
    products = []
    i = int(0)
    for j in range(int(N)):
        p = int(1)
        for k in range(int(N)):
            if j == k:
                p *= (amount[j]-int(K))
            else:
                p *= amount[k]
        products.append(p)
    finalresults.append(max(products))
print(*finalresults,sep='\n')
