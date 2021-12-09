#include<stdio.h>
#include<string.h>
#define MAXN 100000
int last,cur,next[MAXN];
char s[MAXN];
/*This_is_a_[Beiju]_text*/
int main()
{
	while(scanf("%s",s+1)==1){
		int n=strlen(s+1);
		last = cur = 0;
		next[0]=0;
		int i;
		for(i=1;i<=n;i++){
			char ch=s[i];
			if(ch=='['){
				cur=0;
			}else if(ch==']'){
					cur=last;
				}else{
					next[i]=next[cur];
					next[cur]=i;
					if(cur==last){
						last=i;
					}
					cur=i;
				}
			}
		for(i=next[0];i!=0;i++){
			printf("%c",s[i]);
			printf("\n");
		}
	return 0;
	}
}
