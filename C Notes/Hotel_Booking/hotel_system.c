// Problem Statement : Create hotel booking system with following tasks :
// 1. Show all the available room packages to user
// 2. ask user name
// 3. ask user which room they want to enroll
// 4. get the number of days user want the room to be booked
// 5. to show total amount needs to be paid by user
#include <stdio.h> // system library

int main(){ // entry point for C
    char name[50]; // variable --> to store data
    int age, room, days;
    printf("Welcome to our Hotel, \nWhat's your name?\n"); // printf --> used to print anything on screen
    scanf("%s", name); // scanf --> used to accept input from user
    printf("What's your age?\n");
    scanf("%d", &age);
    printf("Thanks %s, your age is %d\n", name, age);
    printf("We have 3 rooms available : 1. Basic-1000/day, 2. Premium-2000/day, 3. Royal-3000/day.\n");
    printf("Please select your room choice and enter your number of days : \n");
    scanf("%d", &room);
    scanf("%d", &days);
    if(room == 1){
        printf("Your total amount : %d", 1000*days);
    }else if(room == 2){
        printf("Your total amount : %d", 2000*days);
    }else if(room == 3){
        printf("Your total amount : %d", 3000*days);
    }else{
        printf("Select correct room choice!");
    }
}

// compiler --> used to check syntax and convert plain english code to binary file