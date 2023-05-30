#include <iostream>
#include <string>
#include <queue>

using namespace std;
int map[101][101] = {0, };
bool visited[101] = {false, };
int N, M;
int cnt = -1;

void dfs(int x){

    queue<int> q;
    q.push(x);
    visited[x] = true;
    

    while(!q.empty()){
        int x = q.front();
        q.pop();
        cnt++;
        for(int i = 1; i<= N; i++){
            if(map[x][i] == 1 && visited[i] == false){
                visited[i] = true;
                q.push(i);
                
            }
        }

    }
    

}

int main(){
    // 컴퓨터 수
    cin >> N;
    // 간선의 수
    cin >> M;

    for(int i = 0; i < M; i++){
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
        map[b][a] = 1;
    }


    dfs(1);
    cout << cnt << endl;
}