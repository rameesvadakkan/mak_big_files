#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[]={10,20,30,40};
    int i;
    for(i=0;i<4;i++){
       printf("%p \n",&a[i]);
    }
    return 0;
}
