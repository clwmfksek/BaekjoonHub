#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	long long int n;
	cin >> n;
	long long int* arr = new long long int[n + 1];
	if (n == 0) {
		cout << 0;
		return 0;
	}
	else if (n == 1) {
		cout << 4;
		return 0;
	}
	else if (n == 2) {
		cout << 6;
		return 0;
	}
	else {
		arr[0] = 0;
		arr[1] = 4;
		arr[2] = 6;
		for (int i = 3; i <= n; i++) {
			arr[i] = arr[i - 1] + arr[i - 2];
		}
		cout << arr[n];
		delete[] arr;
	}
	return 0;
}