#include <stdio.h> // system library where we have printf and scanf functions

int main(){ // entry point to C
    char name[40]; // string in  C --> array of character data type
    int age;
    printf("Please enter your name : \n"); // this will be printed on the screen
    // scanf("%s", name) --> will fail if provided string has any whitespaces
    scanf("%[^\n]", name); // scanf --> to accept input from user
    
    printf("Enter your age : \n");
    scanf("%d", &age);

    printf("Your name is : %s, age : %d\n", name, age);
}