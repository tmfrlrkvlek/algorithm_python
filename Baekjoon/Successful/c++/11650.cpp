#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool cmpY(const pair<int, int> &a, const pair<int, int> &b){
	return a.second < b.second;
}

int main(void){
	int num;
	scanf("%d", &num);
	vector<pair<int, int> > xy;
	int x1, x2;
	
	for(int i = 0; i < num; i++){
		scanf("%d %d", &x1, &x2);
		xy.push_back(make_pair(x1, x2));
	}
	
	sort(xy.begin(), xy.end(), cmpY);
	sort(xy.begin(), xy.end());
	
	for(int i = 0; i < num; i++){
		printf("%d %d\n", xy[i].first, xy[i].second);
	}
}

//int main(void){
//	int num;
//	scanf("%d",&num);
//	std::vector<int> y[200001];
//	std::vector<int> x[200001];
//	int x1, y1;
//	
//	for(int i = 0; i < num; i++){
//		scanf("%d %d", &x1, &y1);
//		y[y1].push_back(x1);
//	}
//	for(int i = -100000; i <= 100000; i++){
//		if(y[i].empty()) continue;
//		else{
//			for(int j = 0; j < y[i].size(); j++){
//				x[y[i][j]].push_back(i);
//			}
//		}
//	}
//	for(int i = -100000; i <= 100000; i++){
//		if(y[i].empty()) continue;
//		else{
//			for(int j = 0; j < x[i].size(); j++){
//				printf("%d %d\n", i, x[i][j]);
//			}
//		}
//	}
//	
//}
