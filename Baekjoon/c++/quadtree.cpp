#include <iostream>
#include <string>
#define MAX 65
using namespace std;
int N;
int map[MAX][MAX] = {0};

void solve(int x, int y, int size){
    if(size == 1){
        cout << map[x][y];
        return ;
    }
    bool zero = true;
    bool one = true;
    for(int i=x; i < x + size; i++){
        for(int j = y; j < y + size; j++){
            if(map[i][j] == 0) {
                one = false;
            }
            if(map[i][j] == 1){
                zero = false;
            }
        }
        
    }

    if(zero == true){
        cout << 0;
        return ;
    }
    if(one == true){
        cout << 1;
        return ;
    }
    cout << "(";
    solve(x, y, size/2);
    solve(x, y + size/2, size/2);
    solve(x+ size/2, y , size/2);
    solve(x+ size/2, y + size/2, size/2);
    cout << ")";

}

int main(){

    cin >> N;
    string str;
    for(int i=0; i<N; i++){
        cin >> str;
        for(int j = 0; j < N; j++){
            map[i][j] = str[j] - '0';
        }
    }

    // for(int i=0; i<N; i++){
    //     for(int j = 0; j < N; j++){
    //         cout << map[i][j] << " ";
    //     }
    //     cout << endl;
        
    // }

    solve(0, 0, N);
    cout <<"\n";
}