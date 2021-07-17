#include<stdio.h>
int main(){
	int a,b,c,d;
	scanf("%d %d %d %d",&a,&b,&c,&d);
	if(a+b+c+d==0){
		printf("¸ð");
	}
	else if(a+b+c+d==1){
		printf("µµ");
	}
	else if(a+b+c+d==2){
		printf("°³");
	}
	else if(a+b+c+d==3){
		printf("°É");
	}
	else if(a+b+c+d==4){
		printf("À·");
	}
	
}
