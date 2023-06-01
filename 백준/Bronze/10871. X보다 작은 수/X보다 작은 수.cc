#include<iostream>
#include<vector>

using namespace std;



int main() {

	int N, X;
	cin >> N >> X;
	vector<int> A(N);

	for (int j = 0; j < N; j++) {
		cin >> A[j];
	}
	
	int i=0;
	while (i < N) {
		if (A[i] < X) {
			cout << A[i] << " ";
		}
		i++;
	}
}
