#include <stdio.h>

struct Machine{
    int num;
    int source;
};

int main()
{
    struct Machine p[100];
    int input=0,min_loc=101;
    scanf("%d",&input);
    for(int a=0;a<input;a++){
        scanf("%d %d",&p[a].num,&p[a].source);
    }
    for(int b=1;b<=100;b++){
        for(int c=0;c<input;c++){
            if(b==p[c].num){
                printf("%d %d\n",p[c].num,p[c].source);
            }
        }
    }

    return 0;
}
