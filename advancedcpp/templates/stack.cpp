#include <iostream>
#include <stack>
#include <stdio.h>
#include <vector>
#include <cstdlib>
#include <stdexcept>

using namespace std; 

template <class T>
class Stack {
    
    private:
        std::vector<T> elts; 
    public:
        void push(T const& elem); 
        void pop();
        T top() const;
        bool empty() const {
            return elts.empty();
        }

};

// Methods

template <class T>
void Stack<T>::push(T const& elem) {
    // want to append to end 
    elts.push_back(elem); 
}

template <class T> 
void Stack<T>::pop() {
    // pop back or pop front ? 
    // first we want to check if the stack is empty 
    if (elts.empty()) {
        throw out_of_range("Stack is empty");
    }
    // else just pop back 
    elts.pop_back();
}

template <class T>
T Stack<T>::top() const {
    if (elts.empty()) {
        throw out_of_range("Stack is empty");
    }
    return elts.back();
}





