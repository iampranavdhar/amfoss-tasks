N=int(input())
s=input()
count0=0
count1=0
for i in range(0,N):
    if(s[i]== '1'):
        count1+=1
    elif(s[i]=='0'):
        count0+=1
if count1 != count0:
    print(1)
else:
    print(2)

#logic is the program contains only o's and 1's and we are seeing
#how many ones and how many o's are there and if it is equal as 
#they asked that min number of good strings so if we rmove 1 
#digit from it and then that becomes good string and remaining 
#1 digit also bcms good string so it will be 2 or if initially 
#only diff number of digits we print as 1 good string
