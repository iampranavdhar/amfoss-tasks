import math 
 
def least_common_multiple(n):  
    k = 1
    for i in range(1, n + 1):  
        k = int((k * i)/math.gcd(k, i))          
    return k
testcases=int(input())
finalresults=[]
for j in range(testcases):
    n=int(input())
    finalresults.append(least_common_multiple(n))
print(*finalresults,sep='\n')