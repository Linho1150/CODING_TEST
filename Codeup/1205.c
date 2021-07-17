#include<stdio.h>

int main()
{
	double a,b,max=0;
	scanf("%lf %lf",&a,&b);
	if(a+b>max){
		max=a+b;
	}
	if(a-b>max){
		max=a-b;
	}
	if(a*b>max){
		max=a*b;
	}
	if(a/b>max){
		max=a/b;
	}
	if(pow(b,a)>max){
		max=pow(b,a);
	}
	printf("%.6lf",max);
}
