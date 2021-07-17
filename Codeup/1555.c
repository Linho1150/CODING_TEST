#include <stdio.h>

int n;

long long int f(long long int n)
{
    long long int a,sum=0;
    for(a=1;a<=n;a++){
        sum=sum+a;
    }
    return sum;
}
int main()
{
  scanf("%d", &n);
  printf("%lld\n", f(n));
}