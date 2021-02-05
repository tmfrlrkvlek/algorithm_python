// 10282
// Dijkstra's Algorithm

#include <stdio.h>
#include <vector>
#include <utility>

using namespace std;

vector<pair<int, int> > *graph; // 노드들간 관계 대입
int *dist;                      // 노드까지의 거리 체크
bool *selected;                 // 이미 선택된 노드인지 체크

void checkDist(int current){    // 거리 체크하기
    for(int i = 0; i < graph[current].size(); i++){
        int v = graph[current][i].first;
        int d = graph[current][i].second;
        if(dist[current] + d < dist[v]){                            // 현재 거리보다 더 짧다면 dist에 거리 대입
            if(dist[v] != 2000000000){                              // 만약 이미 방문됐던 노드면 고쳐진 값을 기준으로 다시 checkDist
                dist[v] = dist[current] + d;        
                checkDist(v);
            }else{                                                  
                dist[v] = dist[current] + d;
            }
        }
    }
}

void dijkstra(int n, int start){    //  Digkstra's Algorithm
    
    dist = new int[n + 1];
    fill(&dist[0], &dist[n + 1], 2000000000);
    dist[start] = 0;
    selected = new bool[n + 1];
    fill(&selected[0], &selected[n + 1], false);
    selected[start] = true;
    int current = start;

    for(int k = 1; k < n; k++){
        checkDist(current);                                         // current와 연결된 노드들까지의 거리 체크
        int small = 0;
        for(int i = 1; i < n + 1; i++){
            if(selected[i] == false && dist[i] != 2000000000){      // 연결되었으나 한번도 선택되지 않은 노드가 있는지 확인
                small = i;
                break;
            }
        }
        if(small == 0){                                             // 그런 노드가 없다면 break;
            break;
        }
        for(int i = small; i < n + 1; i++){                         // 그런 노드가 있다면, 가장 가까운 거리인 노드 선택
            if(selected[i] == false && dist[i] < dist[small]){
                small = i;
            }
        }
        selected[small] = true;                                     // 해당 노드를 기준으로 다시 반복
        current = small;
    }
    int cnt = 0;
    int time = 0;
    for(int i = 1; i < n + 1; i++){
        if(selected[i] == true){
            cnt++;
            if(dist[i] > time){
                time = dist[i];
            }
        }
    }
    printf("%d %d\n", cnt, time);
    
    delete[] dist;
    delete[] graph;
}

int main(void){
    int t;                                  // 테스트 케이스 개수 
    scanf("%d", &t);

    while(t--){
        int n, d, c;                        //  컴퓨터 개수, 의존성개수, 해킹당한 컴퓨터의 번호
        scanf("%d %d %d", &n, &d, &c);  
        graph = new vector<pair<int, int> >[n + 1];
        for(int i = 0; i < d; i++){
            int a, b, s;                    // 컴퓨터 a가 컴퓨터 b를 의존함. b가 감염될 경우 s초 후 a도 감염됨.
            scanf("%d %d %d", &a, &b, &s);
            graph[b].push_back(make_pair(a, s));
        }
        
        dijkstra(n, c);
    }
}

