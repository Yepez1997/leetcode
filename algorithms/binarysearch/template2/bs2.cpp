#include <iostream>
#include <vector>

using namespace std;

template <class T>
T binarySearchTemplate2(vector<T> arr, T target) {
    int left = 0;
    int right = arr.size() - 1;
    int mid;
    while (left <= right) {
        mid =  left + (right - left) / 2; // prevents overloading 
        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid; 
        }
    }
    if (left != arr.size() && arr[left] == target) {
        return left;
    }
    return -1;
}

int main() {
    return 0;
}