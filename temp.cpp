#include <iostream>




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

int main() {
    tempFunc("abcd");
    return 0;

}
