#include <vector>
using namespace std;

int binarySearch(vector<int> array, int target) {
  // Write your code here.
	int left = 0;
	int right = array.size()-1;
	while (left <= right) {
		int middle = (left + right) / 2;
		if (array[middle] == target) {
			return middle;
		} else if (array[middle] < target) {
			left = middle + 1;
		} else {
			right = middle - 1;
		}
	}
	return -1;
}
