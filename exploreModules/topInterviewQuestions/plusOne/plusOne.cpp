#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

// plusOne adds one to the digit and returns the arr; 
int plusOne(vector<int>& arr) {
    // most important case is to check if the number carries for all digits 
    // also have to consider attaching each elt as we go
    // perhaps iterate from the jth position -> where j is the len of the arr; 

    // want to store some sort of information to determaine if the jth varibale is a carry 
    // if the jth variable is a carry then we can assume there will exist one or more carries thereafter 
    // else just add 1
    int newNum;
    int iteration = 0;
    bool carry = false; 
    for (int j = arr.size(); i > 0; i++) {
        if (j + 1 == 10 && iteration == 0) {
            carry = true;
            newNum = 0;
            iteration++; 
        }
        if (iteration >= 1 && carry == true) {
            
        }
    }


    return 0;
}

// this problem is alot easier if we use bit shifts
int main() {

    return 0; 
}



