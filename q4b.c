#include <stdio.h>
#include <math.h>
int main(int argc, char **argv)
{   int a,b,c,d;
    double convert;
	printf("enter any three numbers\n");
    scanf("%d%d%d",&a,&b,&c);
    
    d=a*b*c;
    convert=d*(pow(0.3048,3));
    printf("%d is volume\n",d);
    printf("convert value is%f\n", convert);
	return 0;
}

