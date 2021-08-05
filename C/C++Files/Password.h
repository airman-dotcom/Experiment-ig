#include <iostream>
//Funcation
std::string PasswordChecker(){
std::string password;
std::cout<<"Type in a Password: ";


std::cin >> password;




int passwordlength =  password.length();

if(passwordlength>= 7)
std::cout<<"Strong Password"<<std::endl; 
else
std::cout<<"Weak Password";


    return "Password Was returned";
}




