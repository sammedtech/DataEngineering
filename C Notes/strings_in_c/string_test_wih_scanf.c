#include <stdio.h> // system library that has printf and scanf function in it

int main() {
   char str1[100]; // character array --> used to store text value  or string

   printf("Enter a string: ");
   scanf("%[^\n]", str1); 
   // %[^\n] --> this will help you accept string values from user input
   // even if it consists of any spaces in between string 
   // for example : "Hello World!"

   printf("The string entered is: %s\n", str1); // \n --> used to add new line

   return 0; // it's okay if you don't write this line, as compiler will internally write the same line
}