print("INPUT THREE NUMBERS")
A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))
x = -5
while True:
	y = A*(x*x) + (B*x) + C
	print('y =', x,y)
	x = x+1
	if(x>5):
		break
