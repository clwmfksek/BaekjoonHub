#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int n, k;
	cin >> n >> k;
	int* arr = new int[n];
	fill(arr, arr + n, -1);
	vector<int> v;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	int cnt = 0;
	int target = 0;
	bool bol = false;
	for (int i = 0; i < n; i++) {
		target = v[target];
		cnt++;
		if (target == k) {
			bol = true;
			break;
		}
	}
	if (bol) {
		cout << cnt;
	}
	else {
		cout << -1;
	}
}