//16940

#include <stdio.h> 

bool checkOrganized(vector<int> array[]){
	if(array[3][3] != 0) return false;
	else{
		int idx = 1;
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				if (idx == 10) break;
				if(array[i][j] != idx){
					return false;
				}
				idx++;
			}
		}
	}
} 

int main(void){
	vector<int> array[3];
	int zero[2] = {0};
	
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			int n;
			scanf("%d", &n);
			array[i].push_back(n);
			if(n == 0){
				zero[0] = i;
				zero[1] = j;
			}
		}
	}
	
	while(!checkOrganized(array)){
		// ºó Ä­¿¡ °¡Á®¿Ã ÀÎÁ¢ÇÑ Ä­ Ã£±â.. 
	}
	
	

}
