#include <stdio.h>
#include <string.h>

#define MYNAME "Jean Michel"
int globalVar = 100;

int main(void)
{

    char my_name[100];
    char middleInitial;

    scanf("%s", my_name);
    printf("Your name is %s \n", my_name);
}