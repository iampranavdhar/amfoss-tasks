#include <stdio.h>
#include <string.h>

int main (void)
{
    int n;
    do
    {
        printf("Number of Rows:");
        scanf("%d", &n);
    }
    while (n%2==0);

    int k=(n+1)/2;
    for(int row=1; row <= k; row++)
    {
        for(int stars=k-row; stars>=1; stars--)
        {
            printf("*");
        }
        for(int i=1; i<=(2*row)-1; i++)
        {
            printf("D");
        }

        for(int stars=k-row; stars>=1; stars--)
        {
            printf("*");
        }

        printf("\n");
    }

    for(int row=k-1; row>=1;row--)
    {
        for(int stars=1; stars<=k-row; stars++)
        {
            printf("*");
        }

        for(int i=1; i<=(2*row)-1; i++)
        {
            printf("D");
        }

        for(int stars=1; stars<=k-row; stars++)
        {
            printf("*");
        }
        printf("\n");
    }
}
