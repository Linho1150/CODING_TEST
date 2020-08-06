#include <stdio.h>
int main()
{
	int a;
    scanf("%d",&a);
    if(a%6==0 || (50<=a && a<=70)){
    	printf("win");
	}
	else {
		printf("lose");
	}
}
