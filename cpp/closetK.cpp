#include <cmath>


using namespace std;


class Solution {
public:
  
    // computing the eucladian distance can be computed on constant time 
    double computeEucladianDistance(vector<int> j) {
      return double(sqrt(pow(j.at(0), 2) + pow(j.at(1), 2)));
    }
      
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<vector<int>> closestPoints; 
        typedef pair<double, vector<int>> distances;
        priority_queue<distances, vector<distances>, greater<distances> > pq;
        double distance; 
        for (int j = 0; j < points.size(); j++) {
            distance = computeEucladianDistance(points.at(j));
            pq.push(make_pair(distance, points.at(j)));
        }
        while (K != 0) {
            closestPoints.push_back(pq.top().second);
            pq.pop();
            K--;
        }
        return closestPoints;
        
    }
};
