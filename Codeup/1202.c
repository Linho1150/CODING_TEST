#include<stdio.h>

int main(){
	int a;
	scanf("%d",&a);	
	if(90<=a){
		printf("A");
	}
	else if(80<=a && a<90){
		printf("B");
	}
	else if(70<=a && a<80){
		printf("C");
	}
	else if(60<=a && a<70){
		printf("D");
	}
	else if(a<60){
		printf("F");
	}
}
/*
90점 이상 : A
80점 이상 : B
70점 이상 : C
60점 이상 : D
60점 미만 : F
*/



