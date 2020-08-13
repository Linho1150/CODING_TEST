#include<stdio.h>
int main()
{
	double a,b,temp,result;
	scanf("%lf %lf",&a,&b);
	
	if(a<150){
		temp=a-100;
	}
	else if(150<=a && a < 160){
		temp=(a-150)/2.0+50;
	}
	else if(160<=a){
		temp=((a-100)*0.9);
	}
	result=(b-temp)*100.0/temp;
	
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
