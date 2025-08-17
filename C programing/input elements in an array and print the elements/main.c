#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[100],n,i;
    printf("Enter the numbers of input in array:");
    scanf("%d",&n);
    printf("Enter %d numbers:",n);
    for (i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("The numbers are in array:\n");
         for (i=0;i<n;i++){
        printf("%d ",a[i]);
    }
    printf("\n");

    return 0;
}
