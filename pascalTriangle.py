def pascalTriangle(n):
	if n == 0:
		return([1])
	else:
		prevRow = pascalTriangle(n-1)
		nRow = []
		for (i,num) in enumerate(prevRow):
			if i == 0:
				nRow.append(prevRow[i])
			else:
				nRow.append(prevRow[i]+prevRow[i-1])

				
		nRow.append(1)
		return(nRow)

while True:
	n = int(input('Give n:'))
	print(",".join([str(x) for x in pascalTriangle(n)]))
