#include <stdio.h>
#include <stdlib.h>

int main()
{
    char op;
    float num1,num2,result;
    printf("Enter a operator(+,-,*,/):");
    scanf(" %c",&op);
    printf("Enter 2 numbers: ");
    scanf("%f %f",&num1,&num2);
    switch(op)
    {
    case '+':
        result=num1+num2;
        printf("Result:%.2f\n",result);
        break;
     case '-':
        result=num1-num2;
        printf("Result:%.2f\n",result);
        break;
    case '*':
        result=num1*num2;
        printf("Result:%.2f\n",result);
        break;
    case '/':
        if (num2 != 0) {
                result = num1 / num2;
                printf("Result: %.2f\n", result);
            } else {
                printf("Error: Division by zero!\n");
            }
            break;
    default:
        printf("Invalid operator!\n");
    }
    return 0;
}
