#include <stdio.h>

int main(){ // entry point to your C program
    int whole_number = 10; // declaring integer variable that can store only integer value
    float decimal_number = 11.5; // declaring floating variable, it can store both integer and decimal values
    char alphabets = '$'; // decalaring char variable, it can store any single character
    char text[] = "Akash Ahire, Tushar Dhawale"; // string --> value with more than 1 alphabet or any text
    printf("Integer : %d\nFloating : %f\nCharacter : %c\nString : %s", whole_number, decimal_number, alphabets, text);
    // here 1st %d will be replaced by {whole_number} variable, 2nd %f will be replaced by {decimal_number} variable
    // 3rd %c will be replaced by {alphabets} variable, 4th %s will be replaced by {text} variable
}

