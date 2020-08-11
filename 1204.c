#include<stdio.h>
int main(){
	int a;
	scanf("%d",&a);
	if(a<10){
		if(a==1){
			printf("1st");
		}
		else if(a==2){
			printf("2nd");
		}
		else if(a==3){
			printf("3rd");
		}
		else{
			printf("%dth",a);
		}
	}
	else if(10<a && a<=20){
		printf("%dth",a);
	}
	else
	{
		if(a%10==1){
			printf("%dst",a);
		}
		else if(a%10==2){
			printf("%dnd",a);
		}
		else if(a%10==3){
			printf("%drd",a);
		}
		else
		{
			printf("%dth",a);
		}
	 } 
}
