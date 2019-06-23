#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
struct factor{
	int n;
	int num;
	factor(){num=0;}
};
int main(){
	//首先获得质数表
	int prime[40]={0},k=0;
	int hash[101]={0};//先默认都是质数
	for(int i=2;i<101;i++){
		if(hash[i]==0){
			prime[k++]=i;
			for(int j=i+1;j<101;j++){
				if(j%i==0) hash[j]=1;
			}
		}
	}
	factor fa[12];int f=0;

	int m;cin>>m;int temp=m;

	for(int l=0;l<int(sqrt(1.0*m));l++){
		if(m%prime[l]==0){
			fa[f].n=prime[l];

			while(m%prime[l]==0){
				m=m/prime[l];fa[f].num++;
			}
			f++;
		}
	}
	if(m!=1) {fa[f].n=m;fa[f++].num++;}
	
	for(int x=0;x<f-1;x++){
		printf("%d^%d+",fa[x].n,fa[x].num);
	}
	printf("%d^%d=%d",fa[f-1].n,fa[f-1].num,temp);
	return 0;
}