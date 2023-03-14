#include <stdio.h> // importing system library

int main(){ // entry point in C
    printf("%d \n", 1*1); // \n --> new line
    printf("%d \n", 2*2);
    printf("%d \n", 3*3);
    printf("%d \n", 4*4);
    printf("%d \n", 5*5);
    printf("%d \n", 6*6);
    printf("%d \n", 7*7);
    printf("%d \n", 8*8);
    printf("%d \n", 9*9);
    printf("%d \n", 10*10);

    printf("###############################\n");
    
    // Synatx for loop : for(initialize a variable; condition; increment/decrement)
    for(int i = 5; i <= 10; i++){ // i++ --> i = i + 1, i-- --> i = i - 1
        printf("%d\n", i*i);
    }
}