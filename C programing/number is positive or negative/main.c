#include <stdio.h>
#include <stdlib.h>

int main()
{   int num1;
    printf("Enter number:");
    scanf("%d",&num1);
    if(num1>=0)
    {
        printf("Number is positive");
    }
    else
        {
        printf("Number is Negative");
    }

    return 0;
}
