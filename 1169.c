#include<stdio.h>
int main(){
	int a;
	scanf("%d",&a);
	if(2012-a<1999){
		printf("%d %d",2013-a-1900,1);
	}
	else{
		printf("%d %d",2013-a-2000,3);
	}
}
