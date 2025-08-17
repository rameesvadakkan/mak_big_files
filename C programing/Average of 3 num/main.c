#include <stdio.h>
#include <stdlib.h>

int main()
{
    float num1,num2,num3,average;
    printf("enter 3 numbers:");
    scanf(" %f %f %f",&num1,&num2,&num3);
    average = (num1+num2+num3)/3;
    printf("Average of three numbers:%.2f",average);
    return 0;
}
