while(n*n!=c)
	{
	    while(y+1<n && !a[x][y+1] )
		     a[x][++y] = ++c;
		while(x+1<n  && !a[x+1][y])
		     a[++x][y] = ++c;
		while(y-1>=0  && !a[x][y-1])//the exact detail, just let the computer to complete
		     a[x][--y] = ++c;
		while(x-1>=0 && !a[x-1][y])//using for to control exact times sometimes canbe difficult, we can applicate while  to tackle the ambiguous staff 
		     a[--x][y] = ++c;
    }
