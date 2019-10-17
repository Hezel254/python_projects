#include <stdio.h>

int main(int argc, char **argv)
{   int a,b,c,d;
    
	printf("enter any three numbers\n");
    scanf("%d%d%d",&a,&b,&c);
    
    d=a*b*c;
    printf("%d is volume\n",d);
	return 0;
}

