#include <stdio.h>

int main(){
    int age; // variable declaration
    for(int i = 1; i <= 10; i++){
        printf("Enter your age : \n");
        scanf("%d", &age);
        printf("\nYour age will be %d after 10 years\n", age+10);
        if(i == 2){
            printf("You're Lucky!\n");
        }
    }
}


// Some basic terminal commands : 
// pwd --> shows your current folder location
// ls --> list all the files and folders
// cd --> Change Directory
