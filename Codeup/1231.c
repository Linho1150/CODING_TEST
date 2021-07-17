#include<stdio.h>
int main(){
	int a,b;
	char c;
	scanf("%d%c%d",&a,&c,&b);
	if(c=='+'){
		printf("%d",a+b);
	}
	else if(c=='-'){
		printf("%d",a-b);
	}
	else if(c=='*'){
		printf("%d",a*b);
	}
	else if(c=='/'){
		printf("%.2f",a*1.0/b);
	}
}
