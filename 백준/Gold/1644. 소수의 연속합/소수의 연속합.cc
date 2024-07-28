#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	int* arr = new int[n + 1];
	vector <int> primes;
	fill(arr, arr + n + 1, 1);
	arr[0] = 0;
	arr[1] = 0;

	for (int i = 2; i <= n; i++) {
		if(arr[i] == 1 ){
			for (int j = i * 2; j <= n; j += i) {
				arr[j] = 0;
			}
		}
	}
	for (int i = 2; i <= n; i++) {
		if (arr[i] == 1) {
			primes.push_back(i);
		}
	}
	int s = 0;
	int e = 0;
	int c = 0;
	while (s <= size(primes) && e <= size(primes)) {
		int sum = 0;
		for (int i = s; i < e; i++) {
			sum += primes[i];
		}
		if (sum == n) {
			c++;
			s++;
		}
		else if (sum < n) {
			e++;
		}
		else {
			s++;
		}
	}
	cout << c << '\n';
	return 0;
}