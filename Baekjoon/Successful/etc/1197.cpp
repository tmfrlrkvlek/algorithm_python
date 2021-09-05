// 1197
// Prim's Algorithm

#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

vector<pair<int, int> > *graph;
bool *selected;
int *dist;
int weight = 0;

int getMin(int v){
	int n;
	for(int i = 1; i < v + 1; i++){
		if(selected[i] == false){
			n = i;
			break;
		}
	}
	for(int i = n + 1; i < v + 1; i++){	
		if(selected[i] == false && dist[i] < dist[n]){
			n = i;
		}
    }
	return n;	
}

void prim(int v){
    int current = 1;
    dist[current] = 0;
    for(int i = 1; i < v + 1; i++){
        int u = getMin(v);
        selected[u] = true;
        if(dist[u] == 1000001){
            printf("error");
            return;
        };
        weight += dist[u];

        for(int j = 0; j < graph[u].size(); j++){
            int nv = graph[u][j].first;
            int distance = graph[u][j].second;
            if(selected[nv] == false && distance < dist[nv]){
                dist[nv] = distance;
            }
        }
    }
    printf("%d", weight);
}

int main(void){
    int v, e;   
    scanf("%d %d", &v, &e);
    selected = new bool[v + 1];
    dist = new int[v + 1];
    graph = new vector<pair<int, int> >[v + 1];
    for(int i = 0; i < v + 1; i++){
        selected[i] = false;
    }
    fill(&dist[0], &dist[v + 1], 1000001);
    for(int i = 0; i < e; i++){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        graph[a].push_back(make_pair(b,c));
        graph[b].push_back(make_pair(a,c));
    }
    prim(v);
}