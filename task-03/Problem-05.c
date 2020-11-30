#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N,M;
    do
    {
        scanf("%i %i", &N, &M);
    }
    while(N<2 || N>100000 || M< -100000000 || M>100000000);

    int i;
    int *input;

    input=malloc(N*sizeof(int));
    for(i=0; i<N; i++)
    {
        do
        {
            scanf("%d",&input[i]);
        } 
        while (input[i]< -10000000 || input[i]>10000000);
        
    }

    for (int j=0;j<N;j++)
    {
        for(int k=j+1; k<N; k++)
        {
            if(input[j]+input[k]==M)
            {
                printf("True");
                return 0;
            }
        }
    }
    printf("False");
    return 0;
}
