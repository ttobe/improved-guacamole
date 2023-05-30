#include <iostream>
#include <vector>
#include <queue>
#define MAX 1001
using namespace std;
bool visited[MAX] = {false, };
bool visited2[MAX] = {false, };
int map[MAX][MAX];
int N, M, V;

void dfs(int x){

    visited[x] = true;
    cout << x << " ";

    for (int i = 1; i <= N; i++){
        int y = map[x][i];
        
        if(visited[i] == false && y == 1){
            dfs(i);
        }
    }
    
}

void bfs(int start) {
    queue<int> q;
    q.push(start); // 첫 노드를 queue에 삽입
    visited2[start] = true; // 첫 노드를 방문 처리

    // 큐가 빌 때까지 반복
    while (!q.empty()) {
        // 큐에서 하나의 원소를 뽑아 출력
        int x = q.front();
        q.pop();

        cout << x << ' ';

        // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for (int i = 1; i <= N; i++) {
            int y = map[x][i];
            if (visited2[i] == false && y == 1) {
                q.push(i);
                visited2[i] = true;
            }
        }
    }
}

int main(){
    
    cin >> N >> M >> V;
    vector<int> graph[10];

    for (int i = 0; i < M; i++){
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
        map[b][a] = 1;
    }

    dfs(V);
    cout << endl;

    bfs(V);
    cout << endl;


}