// Arrays
// array is a variable holding similar type of data

#include <stdio.h>

int main(){
    int topper1 = 10;
    int topper2 = 20;
    int topper3 = 30;

    // int sal[10]; // variable declaration and it's an integer array that can hold 10 integer values
    int sal[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}; // variable definition
    // array position start from 0
    printf("%d\n", sal[0]);
    printf("%d\n", sal[1]);
    printf("%d\n", sal[2]);
    printf("%d\n", sal[3]);
    printf("%d\n", sal[4]);
    printf("%d\n", sal[5]);
    printf("%d\n", sal[6]);
    printf("%d\n", sal[9]);
    printf("#######################\n");
    for(int i = 0; i < 10; i++){
        printf("%d\n", sal[i]);
    }
}