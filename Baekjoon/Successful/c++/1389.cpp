// 1389
// floyd-warshall algorithm

#include <stdio.h>
#include <iostream>

using namespace std;

int main(void){
	int n, m;
	scanf("%d %d", &n, &m);
	int relation[n][n] = {0,};
	fill(&relation[0][0], &relation[n - 1][n], 9999);
	for(int i = 0; i < m; i++){
		int p1, p2;
		scanf("%d %d", &p1, &p2);
		relation[p1 - 1][p2 - 1] = 1;
		relation[p2 - 1][p1 - 1] = 1;
	}
	for(int k = 0; k < n; k++){
		for (int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(	relation[i][j] > relation[i][k] + relation[k][j]){
					relation[i][j] = relation[i][k] + relation[k][j];
				}
			}
		}
	}
	for(int i = 0; i < n; i++){
		for(int j = 1; j < n; j++){
			relation[i][0] += relation[i][j];
		}
	}
	int p = 0;
	for(int i = 1; i < n; i++){
		if(relation[i][0] < relation[p][0]) p = i;
	}
	printf("%d", p + 1);
}
