// 9370
// Dijkstra's Algorithm..?

#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

vector<pair<int, int> > *graph;
int *dist;
int *Gdist;
int *Hdist;
int *beforeNode;
int n, t, s, g, h;
queue<int> q;
int ghdist;

void checkCan(int start, int end){
    if(dist[end] == dist[g] + ghdist + Hdist[end]){
        printf("%d ", end);
    }else if(dist[end] == dist[h] + ghdist + Gdist[end]){
        printf("%d ", end);
    }
}

void checkDist(int current, int* Kdist){
    for(int i = 0; i < graph[current].size(); i++){
        int v = graph[current][i].first;
        int d = graph[current][i].second;
        if(Kdist[current] + d < Kdist[v]){
            beforeNode[v] = current;
            q.push(v);
            Kdist[v] = Kdist[current] + d;
        }
    }
}

// 시작점, 도착점, 총 노드개수 입력 시 시작점과 도착점 간 노드 출력
void dijkstra(int start, int* Kdist){
    Kdist[start] = 0;
    beforeNode[start] = start;
    q.push(start);
    while(!q.empty()){
        int current = q.front();
        q.pop();
        checkDist(current, Kdist);
    }
}


int main(void){
    int test;
    scanf("%d", &test);
    while(test--){
        int m;
        scanf("%d %d %d", &n, &m, &t);
        vector<int> candidate;
        beforeNode = new int[n + 1];
        dist = new int[n + 1];
        Hdist = new int[n + 1];
        Gdist = new int[n + 1];
        for(int i = 0; i < n + 1; i++){
            dist[i] = 2000000000;
            Hdist[i] = 2000000000;
            Gdist[i] = 2000000000;
        }
        graph = new vector<pair<int, int> >[n + 1];
        scanf("%d %d %d", &s, &g, &h);
        for(int i = 0; i < m; i++){
            int a, b, d;
            scanf("%d %d %d", &a, &b, &d);
            graph[a].push_back(make_pair(b, d));
            graph[b].push_back(make_pair(a, d));
        }
        for(int i = 0; i < t; i++){
            int c;
            scanf("%d", &c);
            candidate.push_back(c);
        }
        sort(candidate.begin(), candidate.end());
        dijkstra(s, dist);
        dijkstra(g, Gdist);
        ghdist = Gdist[h];
        dijkstra(h, Hdist);
        for(int i = 0; i < t; i++){
            checkCan(s, candidate[i]);
        }
        printf("\n");
    }
}