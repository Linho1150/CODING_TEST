#include<stdio.h>
int main(){
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	if(a>b){
		if(b>c){
			printf("%d",b);
		}
		else{
			if(a>c){
				printf("%d",c);	
			}
			else
			{
				printf("%d",a);
			}
			
		}
	}
	else{ //a<b
		if(b>c)//a<b , c<b
		{
			if(a>c){ //c<a<b
				printf("%d",a);
			}
			else
			{
				printf("%d",c);
			}
		}
		else{
			printf("%d",b);
		}
	}
}
