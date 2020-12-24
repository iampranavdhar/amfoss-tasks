n,k=input().split()
idsofhouses=list(map(int,input().split()))
orders=list(map(int,input().split()))
finalresults=[]
for i in range(len(orders)):
#As it should take the largest place first i came from the reverse direction.
    for j in range(len(idsofhouses)-1,-1,-1):
        if orders[i]==idsofhouses[j]:
            finalresults.append(j+1)
            idsofhouses[j]= -1 
#when i am not doing this as it is the first elemnt that occurs
#everytime for that respective id i am getting that same result
#multiple times so i decided to change it to some random element
#which can not be there in the list.
            break
    else:
        finalresults.append(-1)
print(*finalresults)


