#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num1;int num2;int num3;
    printf("Enter 1st num:");
    scanf("%d",&num1);
     printf("Enter 2nd num:");
    scanf("%d",&num2);
    num3=num1;
    num1=num2;
    num2=num3;
    printf("swaped numbers num1:%d num2:%d \n",num1,num2);
    //without third variable//
    num1=num1+num2;
    num2=num1-num2;
    num1=num1-num2;
    printf("Again swapped with out var num1:%d num2:%d",num1,num2);
    return 0;
}
