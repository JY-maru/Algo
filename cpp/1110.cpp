#include<iostream>
#include<math.h>
using namespace std;

int main(){
	int num;
	cin >> num;
	int pivot = num;
	int temp;
	int cnt = 1;
	while(1){
		temp  = 10*(pivot%10) + (pivot/10 + pivot%10)%10;
		pivot = temp;	
		if(num == temp){
				break;
		}
		cnt ++;
	}
	cout << cnt ;
}
