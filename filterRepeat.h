for(i=1; i<n; i++){
		for(j=0; j<i; j++){
			if(c[i]==c[j])
				break;
		}
		if(j>=i)
			printf(" %d", c[i]);
	}
