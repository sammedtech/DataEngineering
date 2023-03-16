#include <stdio.h> // system library that contains printf and scanf functions

// void square(int xyz){
int square(int xyz){
    printf("The input is : %d\n", xyz);
    return xyz*xyz; // this function returning some integer value
}

int main(){
    int result = square(20); // calling a function and storing the value returned by function in a variable
    printf("The final result : %d\n", result);

    return 0; // this is line will be added by compiler internally
}