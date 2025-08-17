#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char letter1,letter2,letter3,letter4;
    printf("Enter 4 letters : \n");
    scanf(" %c",&letter1);
    scanf(" %c",&letter2);
    scanf(" %c",&letter3);
    scanf(" %c",&letter4);
    printf("The word is :%c%c%c%c",letter1,letter2,letter3,letter4);
    return 0;
}
