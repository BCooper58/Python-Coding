def ranchar():
	r = randchar("A","Z")
	return r
	
def main():
	for r in range (10):
		rchar = ranchar()
		print (rchar, end="")
		
main()

