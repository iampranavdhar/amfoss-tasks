import math  
def maxPrimeFactors (a): 
	maxx = -1 
	while a % 2 == 0: 
		maxx = 2
		a = a/2	 
	for i in range(3, int(math.sqrt(a)) + 1, 2): 
		while a % i == 0: 
			maxx = i 
			a = a / i 
	if a > 2: 
		maxx = a 
	return int(maxx)
testcases=int(input())
finalresults=[]
for i in range(testcases):
    N=int(input())
    finalresults.append(maxPrimeFactors(N))
print(*finalresults,sep='\n')



