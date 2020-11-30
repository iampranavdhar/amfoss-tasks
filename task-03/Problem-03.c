#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    do
    {
        scanf("%i", &N);
    }
    while(N < 1 || N > 10^6);
    

    int *input1;

    input1=malloc(N*sizeof(int));
    for(int i=0; i<N; i++)
    {
        do
        {
            scanf("%d", &input1[i]);
        }
        while(input1[i]<1 || input1[i]>10^9);
    }

    int *input2;

    input2=malloc(N*sizeof(int));            // we used malloc i.e memory allocation bcz the size of the array is fixed.
    for(int i=0; i<N; i++)
    {
        do
        {
            scanf("%d", &input2[i]);
        }
        while(input2[i]<1 || input2[i]>10^9); 
    }
    
    int min= 1000000000;                     //he we used min as this instead of 0 bcz 0 is anyway min so when we compare nothing min in that case so we used this. 
    for(int j=0;j<N;j++)
    {
                                            //  printf("%i ",(input2[j]/input1[j]));
        if(input2[j]/input1[j]< min)
        min = (input2[j]/input1[j]);   
    }
    printf("%i", min);
}
