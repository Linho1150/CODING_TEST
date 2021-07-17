#include<stdio.h>
int main(){
	int a,b;
	scanf("%d %d",&a,&b);
	if(b==1 || b==2){
		printf("%d",2012-(a/10000+1900)+1);
	}
	else
	{
		printf("%d",2012-(a/10000+2000)+1);
	}
}
