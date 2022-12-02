BEGIN {
	max=0
	sum=0	
}

/[0-9]+/{
	sum+=$1
}

/^$/{
	if(sum>max)
		max=sum
	sum=0
}

END {
	if(sum>max)
		max=sum
	print max
}

