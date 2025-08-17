#include <stdio.h>
#include <stdlib.h>

int main()
{   int number;
    printf("Enter a number:");
    scanf("%d",&number);
    if (number==0)
    {
        printf("Number is Zero %d",number);
    }
    else if (number%2==0)
    {
        printf("Number is Even %d \n",number);
    }
    else
    {
        printf("Number is Odd %d",number);
    }
    return 0;
}
