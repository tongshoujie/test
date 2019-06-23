#include<cstdio>
#include<iostream>
using namespace std;
//写一趟快速排序的函数
int pos(int a[],int left,int right){//这里面排序包括了right
	int temp=a[left];
	while(left<right){
		while(left<right&&a[right]>temp) right--;
		a[left]=a[right];
		while(left<right&&a[left]<=temp) left++;
		a[right]=a[left];
	}
	a[left]=temp;
	return left;
}
void quicksort(int a[],int left,int right){//这里面排序包括了right
	if(left<right){//这其实算是递归边界，left=right就不递归了
		int po=pos(a,left,right);
		quicksort(a,left,po-1);
		quicksort(a, po+1,right);
	}

}

int main(){
	int n,a[100]={0};
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	quicksort(a,0,n-1);//因为左右都是包括的
	for(int j=0;j<n;j++){
		cout<<a[j]<<' ';
	}



	return 0;
}
