def print_pascal_row(row):
	topr = ""
	for col in row:
		if col == 0:
			topr +=  " "
		else:
			topr +=  str(col)
	print topr
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	n = int(test.strip())
	pascal = [0] * n
	print_pascal_row(pascal)	
test_cases.close()
