#include <iostream>
#include <exception>
#include <vector>

// templates to allow binary search on any data type
// assume types are sorted   

using namespace std;  


template <class T>
T binarySearchTemplate(vector<T> arr, T target) {
    int left =  0, right = arr.size() - 1;
    int mid; 
    while (left <= right) {
        mid = (left + right) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else { 
            right = mid - 1;
        }
    }
    return -1;
}
 
int main() {
    vector<char> chars; 
    chars.push_back('a');
    chars.push_back('f');
    chars.push_back('d');
    char target =  'f';
    int charFound = binarySearchTemplate(chars, target);
    cout << charFound << endl;

    return 0;
}
