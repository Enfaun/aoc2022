BEGIN {
	count=1
}

/[0-9]+/{
	sum[count]+=$1
}

/^$/{
	count+=1
}

END {
	asort(sum, sum, "@val_num_desc")
	print sum[1]
	print sum[2]
	print sum[3]
	print sum[1]+sum[2]+sum[3]
}

