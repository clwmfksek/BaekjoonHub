#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int x,n;
	cin >> n >> x;
	int arr[100000];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	int start = 0;
	int end = 0;

	int ans = 2000000000;

	while (start < n && end < n) {
		if (arr[end] - arr[start] < x) {
			end++;
		}
		else {
			ans = min(ans, arr[end] - arr[start]);
			start++;
		}
	}
	cout << ans;
	return 0;
}