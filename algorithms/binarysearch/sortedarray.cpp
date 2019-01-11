#include <iostream>
#include <vector>



using namespace std; 


int binarySearch(vector<int> arr, int target) {
    int left = 0; 
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2; // take the middle 
        if (arr[mid] < target) {
            left = mid + 1;
            // if it is less than set mid one more 
        }
        else if (arr[mid] > target) {
            right = mid - 1;
            // if its bigger set mid off by one 
        }
        else {
            return mid;
        }
    }
    return -1; 
}

int main() {
    vector<int> vect;    
    vect.push_back(-1); 
    vect.push_back(0); 
    vect.push_back(3); 
    vect.push_back(5); 
    vect.push_back(9); 
    vect.push_back(12); 
    // [-1,0,3,5,9,12]
    int target = 9;
    int index = binarySearch(vect, target);
    //cout << "index: " << index << endl; 

    return 0;

}




