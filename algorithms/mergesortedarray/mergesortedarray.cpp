/*Problem: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. */
class MergeSortedArrayn {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // subtract one for indexing 
        int i = m - 1, j = n - 1, tar = m + n - 1;
        // tar is the size of the array m + n 
        while (j >= 0) {
            // ternary ops 
            // if x ? true : false 
            nums1[tar--] = i >= 0 && (nums1[i] > nums2[j]) ? nums1[i--] : nums2[j--];
        }
    }
};
