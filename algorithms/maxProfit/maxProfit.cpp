#include <iostream>
#include <vector>

using namespace std;
// BEST TIME TO SELL BUY STOCK 
// check the first elt 
// check if it is less than the next 
// if it is we do a while loop to get a max sum
// and a current running sum 

int maxSumArray(vector<int> &arr) {
    int low; 
    int runningSum = 0; 
    int maxProfitSum = 0;
    int current; 
    for (int i = 0; i < (int)arr.size(); i++) {
        low = arr[i]; 
        current = low;
        while (low <= arr[current] && current < (int)arr.size() - 1) {
            runningSum = arr[current + 1] - low; 
            if (runningSum > maxProfitSum) {
                maxProfitSum = runningSum;
            }
            current++;
        }
        runningSum = 0; 
    }
    return maxProfitSum;
}


int main() {
    vector<int> arr; 
    arr.push_back(7);
    arr.push_back(1);
    arr.push_back(5);
    arr.push_back(3);
    arr.push_back(6);
    arr.push_back(4);
    int maxStockProfit = maxSumArray(arr);
    cout << maxStockProfit << endl;
    return 0;
};