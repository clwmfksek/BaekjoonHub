#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> nums(n);
    for(int i = 0; i < n; ++i){
        cin >> nums[i]; 
    }

    vector<int> result;

    for(int i = n; i >= 1; --i){
        int pos = nums[i-1];
        result.insert(result.begin() + pos, i);
    }

    for(auto num : result){
        cout << num << "\n";
    }

    return 0;
}
