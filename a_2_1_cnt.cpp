#include<string.h>
#include<stdio.h>


int main()
{
	char s[7][10];
	char a[7][10];
	char temp[10];
	int cnt=0;

	while(scanf("%s %s %s %s %s %s",s[0],s[1],s[2],s[3],s[4],s[5])!=EOF){
	printf("CASE %d:\n",cnt++);
	for(int i=0;i<10;i++)
	{
		scanf("%s %s %s %s %s %s",a[0],a[1],a[2],a[3],a[4],a[5]);
		for(int j=0;j<6;j++){
			if(strcmp(a[j],s[j])==0) printf("1 ");
			else printf("0 ");
		}
		printf("\n");
	}
	}
	return 0;
}