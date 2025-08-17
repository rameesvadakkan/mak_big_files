#include <stdio.h>
#include <stdlib.h>

int main()
{
     int i,j,rows=4;
     for(i=1;i<=rows;i++)
     {
         for(j=rows;j>=i;j--)
         {
             printf("* ");
         }
           printf("\n");
     }
     return 0;
}
