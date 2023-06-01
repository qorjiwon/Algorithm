#include<iostream>

using namespace std;

int main() {
	string s, X="abcdefghijklmnopqrstuvwxyz";
	cin >> s;
	for (int i = 0; i < X.length(); i++) {
		int x = 0;
		for (int j = 0; j < s.length(); j++) {
			if (s[j] == X[i]) x++;
		}
		cout << x << " ";
	}
}