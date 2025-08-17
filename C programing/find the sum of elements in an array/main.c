#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[]={10,20,30,15},i,sum=0;
    int n= sizeof(a)/sizeof(a[0]);
    for(i=0;i<n;i++)
    {
        sum+=a[i];
    }
    printf("Sum of elements : %d",sum);

    return 0;
}
