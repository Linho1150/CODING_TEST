#include<stdio.h>
int main()
{
	double a,b,temp,result;
	scanf("%lf %lf",&a,&b);
	temp=((a-100)*0.9);
	result=(b-temp)*100/temp;
	
	if(result <= 10){
		printf("정상");
	}
	else if(10<result && result <=20){
		printf("과체중");
	}
	else{
		printf("비만");
	}
}
