#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[] = {10,15,20,25};
    int i;
    a[0]=50;
    int n = sizeof(a)/sizeof(a[0]);
    for (i=0;i<n;i++){
        printf("%d ",a[i]);
    }

    return 0;
}
