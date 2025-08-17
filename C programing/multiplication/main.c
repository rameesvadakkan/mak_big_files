#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num,result;
    int multi()
    { printf("enter a number");
      scanf(" %d",&num);
        for(int i=1;i<=10;i++){
            result=i*num;
            printf(" %dx%d=%d \n",i,num,result);
        }

    }
    multi();
    multi();
    return 0;
}
