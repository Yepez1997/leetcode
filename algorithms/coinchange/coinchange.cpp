class Solution {
public:
        int coinChange(vector<int>& coins, int amount) {
        vector<int> v(amount+1,amount+1);
        v[0]=0;
        for(int i=0;i<coins.size();i++){
            for(int j=coins[i];j<=amount;j++){
                v[j]=min(v[j],v[j-coins[i]]+1);  
            }
        }
            
        for (int i : v) {
            cout << i << endl; 
        }
            
        if(v[amount]==amount+1)
            return -1;
    
        return v[amount];
    }
};
