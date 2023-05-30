// 2178 미로 탐색
#include <iostream>
#include <string>
#include <queue>

using namespace std;
int N, M;
int map[101][101];
bool visited[101][101] = {false, };

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int x, int y){
    
    queue<pair<int, int>> q;
    q.push({x, y});
    while(!q.empty()){

        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        // cout << x << y << endl;
        for (int i = 0; i < 4; i++){

            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx <0 || nx >= N || ny < 0|| ny >= M){
                continue;
            }
            if (map[nx][ny] == 0){
                continue;
            }
            if(map[nx][ny] == 1){
                map[nx][ny] = map[x][y] + 1;
                q.push({nx,ny});
            }
        }


    }
    
    

}



int main(){

    cin >> N >> M;
    string str;
    // for(int i = 0; i < N; i++){
        
    //     cin >> str;

    //     for (int j = 0; j < M; j++){
    //         map[i][j] = str[j] - '0';
    //     }
    // }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%1d", &map[i][j]);
        }
    }

    bfs(0, 0);
    cout << map[N-1][M-1] << endl;
}