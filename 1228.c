#include<stdio.h>
int main()
{
	double a,b,temp,result;
	scanf("%lf %lf",&a,&b);
	temp=((a-100)*0.9);
	result=(b-temp)*100/temp;
	
	if(result <= 10){
		printf("����");
	}
	else if(10<result && result <=20){
		printf("��ü��");
	}
	else{
		printf("��");
	}
}
