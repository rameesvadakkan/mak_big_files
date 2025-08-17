#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j,rows,s;
    printf("Enter the number of rows:");
    scanf(" %d",&rows);
    for(i=0;i<rows;i++)
    {
        for(s=0;s<rows-i-1;s++)
        {
            printf("  ");
        }
        for(j=0;j<=i;j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
