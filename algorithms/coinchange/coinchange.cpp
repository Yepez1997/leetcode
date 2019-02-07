/* Coin Change using Dynamic Programming */
#include <vector>
#include <map>
#include <iostream>
#include <math.h>


using namespace std;

/* Gets the min number of coins for x amount */
int coinChange(vector<int>& coins, int amount) {
vector<int> v(amount+1,amount+1);
v[0]=0;
for(int i=0;i<coins.size();i++){
    for(int j=coins[i];j<=amount;j++){
        v[j]=min(v[j],v[j-coins[i]]+1);  
    }
}
// solutions that contain the mth coin and solutions that cointain 
// at least the mth coin 
if(v[amount]==amount+1)
    return -1;
return v[amount];
}




