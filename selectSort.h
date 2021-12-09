void sort( int a[], int n )
{
	int i,j,temp,index=0;
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if(a[j]<=a[i]){
				index=j;
				temp=a[i];
				a[i]=a[index];
				a[index]=temp;
			}
		}
	}
}
