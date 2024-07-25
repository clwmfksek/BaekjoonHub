#include <bits/stdc++.h>
using namespace std;

int main(){
  string target;
  int number;
  int result = 0;

  cin >> target;
  cin >> number;

  for(int i=0; i<target.length(); i++){
    if(target[i] <= '9' && target[i] >= '0'){
      result += ((target[i] - '0') * pow(number, target.length() - i - 1));
    }
    else{
      result += ((target[i] - 'A' + 10) * pow(number, target.length() - i - 1));
    }
  }
  cout << result;
}
