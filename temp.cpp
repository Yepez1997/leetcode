#include <iostream>
#include <limits>



using namespace std; 

void tempFunc(string s){ 
    cout << "start" << endl;
    int n = (int)s.size();
    for(int i=n-1; i>=0; i--) {
        for(int j=i; j<n; j++) {
           cout << i + 1 << " " << j - 1 << endl;
    }
  }
}



void numLimitsTests() {
    cout << numeric_limits<double>::max() << endl; 
}


int main() {
    tempFunc("abcd");
    numLimitsTests(); 
    return 0;

}
