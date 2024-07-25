#include <bits/stdc++.h>
using namespace std;
char v[5][15];
int main(){
  for(int i=0; i<5;i++){
      cin >> v[i];
  }

  for(int i=0;i<15;i++){
    for(int j=0;j<5;j++){
      if(v[j][i] != NULL){
        cout << v[j][i];
      }
    }
  }
}