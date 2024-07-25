#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	int arr[100000];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);

	int target1 = 1e9;
	int target2 = 1e9;

	int start = 0;
	int end = n - 1;

	while (start != end) {
		if (abs(arr[start] + arr[end]) < abs(target1 + target2)) {
			target1 = arr[start];
			target2 = arr[end];
		}
		if (arr[start] + arr[end] < 0) {
			start++;
		}
		else {
			end--;
		}
	}
	cout << target1 << " " << target2 << "\n";
	return 0;
}