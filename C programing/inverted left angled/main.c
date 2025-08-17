#include <stdio.h>
#include <stdlib.h>

int main()
{

    int i,j,r=4,s;
    for(i=0;i<r;i++)
    {
        for(s=0;s<i;s++)
        {
            printf("  ");
        }
        for(j=0;j<r-i;j++)
        {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
