#include <stdio.h>

void addition(int a, int b, int age){
    int count = 10; // variable declaration and definition
    int age = 22;
    printf("The value in count : %d\n", count);
    printf("Addition with count : %d\n", a+b+count);
    printf("The value in age : %d\n", age);
}

int main(){
    int age = 22;
    addition(1, 1); // calling a function
}