#include <vector>
#include <stdio.h>
// #include <algorithm>

bool i_knows_j(int i, int j){
	if (j == 5){ return true; }
	else {return false;}
}

int get_famous(int n){
	std::vector<bool> famous(n+1, true);
	std::vector<bool>::iterator it;
	for(int i = 1; i <= n; i++){
		if (famous[i]){
			for(int j = 1; j <= n; j++){
				if(j != i){
					if(i_knows_j(i,j)){
						famous[i] = false;
						break;
					}
					else {famous[j] = false;}
				}
			}
		}
	}
	it = find(famous.begin()+1, famous.end(), true);
	return it - famous.begin();
}

int main(){
	printf("%d", get_famous(10));

}