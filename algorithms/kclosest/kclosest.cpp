#include <iostream>
#include <stack>
#include <queue>
#include <utility>
#include <math.h>


using namespace std; 

typedef pair<double, double> coordinates;
typedef pair<double, coordinates> distances;

void findKNearest(vector<coordinates> arr, int k) {
    double distance; 
    priority_queue<double,vector<double>, greater<double> >  minheap;
    for (int i = 0; i < (int)arr.size(); ++i) {
        distance = sqrt(pow((arr[i].first),2) + pow((arr[i].second),2));
        minheap.push(distance);
    }
    vector<double> res; 
    int count = k;
    while(count != 0) {
        res.push_back(minheap.top());
        cout << minheap.top() << endl;
        minheap.pop();
        --count;
    }

    for (int i = 0; i < (int)res.size(); ++i) {
        cout << res[i] << endl;
    }
}



int main () {

    vector<coordinates> arr; 
    int k = 1;
    arr.push_back(make_pair(1,3));
    arr.push_back(make_pair(2,-2));
    findKNearest(arr, k);


    return 0;
}