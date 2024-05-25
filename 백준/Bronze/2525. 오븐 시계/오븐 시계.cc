#include<iostream>
using namespace std;

int main() {
    int x, y, z;
    cin >> x >> y;
    cin >> z;
    y += z % 60;
    x += y / 60;
    y %= 60;
    x += z / 60;
    x %= 24;
    cout << x << ' ' << y << endl;
    return 0;
}
