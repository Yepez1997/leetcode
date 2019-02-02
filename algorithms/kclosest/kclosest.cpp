#include <iostream>
#include <stack>
#include <queue>
#include <utility>
#include <math.h>


using namespace std; 

typedef pair<double, double> coordinates;
typedef pair<double, coordinates> distances;
// priority q's by default are ordered by the first elt
typedef priority_queue<distances,vector<distances>, greater<distances> >  minheap;

vector<coordinates> findKNearest(vector<coordinates> arr, int k) {
    double distance; 
    minheap pq; 
    for (int i = 0; i < (int)arr.size(); ++i) {
        distance = sqrt(pow((arr[i].first),2) + pow((arr[i].second),2));
        pq.push(make_pair(distance, arr[i]));
    }
    vector<coordinates> results; 
    int count = k;
    while(count != 0) {
        results.push_back(pq.top().second);
        pq.pop();
        --count;
    }
    return results;
}

int main () {

    vector<coordinates> arr; 
    int k = 2;
    arr.push_back(make_pair(3,3));
    arr.push_back(make_pair(5,-1));
    arr.push_back(make_pair(-2,4));
    vector<coordinates> coord =findKNearest(arr, k);

    for(int j = 0; j < (int)coord.size(); ++j) {
        cout << "(" << coord[j].first << ", " << coord[j].second  << ")" << endl;
    }

    return 0;
}
