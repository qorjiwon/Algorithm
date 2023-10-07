#include <iostream>
#include <utility>
#include <queue>
using namespace std;

int m[50][50];
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
int N, M;

void bfs(int x, int y) {
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	m[x][y] = 0;

	while (!q.empty()){
		pair<int, int> current = q.front();
		q.pop();
		x = current.first;
		y = current.second;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (-1 < nx && nx < N && -1 < ny && ny < M && m[nx][ny]) {
				m[nx][ny] = 0;
				q.push(make_pair(nx, ny));
			}
		}
	}
}

int main() {
	int T, K;
	cin >> T;
	while (T--) {
		int ans = 0;
		cin >> M >> N >> K;
		for (int i = 0; i < K; i++) {
			int x, y;
			cin >> y >> x;
			m[x][y] = 1;
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (m[i][j]) { 
					bfs(i, j);
					ans++;
				}
			}
		}
		cout << ans << endl;
	}
	return 0;
}