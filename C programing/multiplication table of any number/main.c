#include <stdio.h>
#include <stdlib.h>

int main()
{
     int num, i;
     printf("Enter a number to print its multiplication table: \n");
     scanf("%d", &num);
     for(i=0;i<=10;i++){
        printf("%d X %d=%d \n\n\t",num,i,num*i);
     }
    return 0;
}
