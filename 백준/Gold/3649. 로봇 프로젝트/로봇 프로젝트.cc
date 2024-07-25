#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int x,n;
	while (cin >> x) {
		x *= 10000000;
		cin >> n;
		vector<int> v(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}
		sort(v.begin(), v.end());

		int start = 0, end = n-1;

		bool bol = true;
		while (start < end) {
			if (v[start] + v[end] == x) {
				cout << "yes " << v[start] << " " << v[end] << '\n';
				bol = false;
				break;
			}
			else if (v[start] + v[end] < x) {
				start++;
			}
			else {
				end--;
			}
		}
		if (bol) {
			cout << "danger" << '\n';
		}
	}
	return 0;
}