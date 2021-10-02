// 10026
// [DFS] 깊이 우선 탐색 적용 

#include <stdio.h>
#include <vector>

using namespace std;

int nSum = 0;							// 적록색약 아닌 사람 기준 구역 수 
int norSum = 0;							// 적록색약인 사람 기준 구역 수 
bool *checked;							// 노드 방문 여부 체크 

void DFS(vector<int> graph[], vector<char> pixels, int idx, int kind){
	if (checked[idx] == true){
		return;
	}
	else{
		if(kind == 0){						// 각 구역별로 처음 DFS를 호출할 때 Sum을 증가시켜 준다. 
			nSum++;
		}else if(kind == 1){
			norSum++;
		}
		checked[idx] = true;
		for(int i = 0; i < graph[idx].size(); i++){
			DFS(graph, pixels, graph[idx][i], 2);	// kind = 2로 설정해 그 다음 DFS 부터는 Sum을 증가시키지 않도록 한다. 
		}
	}
	return;
}

int main(void){
	int n;
	scanf("%d\n", &n);
	vector<int> pictures[n * n + 1];		// 적록색약이 아닌 사람 기준 그래프 
	vector<int> norPictures[n * n + 1];		// 적록색약인 사람 기준 그래프 
	vector<char> pixels;					// 그림 픽셀들 모음 
	pixels.push_back('n');
	checked = new bool[n * n + 1];			 
	checked[0] = {true};
	// 입력 및 그래프 생성 
	for(int i = 0; i < n; i++){
		char pix;
		for(int j = 0; j < n; j++){
			int current = i * n + j + 1; 
			// 픽셀 입력 
			scanf("%c", &pix);
			pixels.push_back(pix);
			checked[current] = false;
			// 그래프 생성 
			if (i != 0){
				if(pixels[current] == 'G' || pixels[current] == 'R'){	
					if(pixels[current - n] == 'G' || pixels[current - n] == 'R'){
						norPictures[current].push_back(current - n);
						norPictures[current - n].push_back(current);
					}
				}else{
					if(pixels[current - n] == pix){
						norPictures[current].push_back(current - n);
						norPictures[current - n].push_back(current);
					}
				}
				if(pixels[current - n] == pix){
					pictures[current].push_back(current - n);
					pictures[current - n].push_back(current);
				}
				
			}
			if (j != 0){
				if(pixels[current] == 'G' || pixels[current] == 'R'){
					if(pixels[current - 1] == 'G' || pixels[current - 1] == 'R'){
						norPictures[current].push_back(current - 1);
						norPictures[current - 1].push_back(current);
					}
				}else{
					if(pixels[current - 1] == pix){
						norPictures[current].push_back(current - 1);
						norPictures[current - 1].push_back(current);
					}
				}
				if(pixels[current - 1] == pix){
					pictures[current].push_back(current - 1);
					pictures[current - 1].push_back(current);
				}
			}
		}
		scanf("%c", &pix);						// 입력된 '\n' 제거 
	}
	
	// 1 ~ 25 노드 모두 한번씩 DFS 실행 - 적록색약 아닌 사람 기준 
	int i = 1;
	while(i != n * n + 1){						
		DFS(pictures, pixels, i++, 0);
	}
	
	// 다음 DFS를 위해 초기화 
	for(i = 1; i < n * n + 1; i++){				
		checked[i] = false;
	}
	i = 1;
	
	// 1 ~ 25 노드 모두 한번씩 DFS 실행 - 적록색약인 사람 기준 
	while(i != n * n + 1){						
		DFS(norPictures, pixels, i++, 1);
	}
	
	// 결과값 출력 
	printf("%d %d", nSum, norSum);
	
}
