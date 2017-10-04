def intcalc():
	i = int(input("I:"))
	a = 5
	b = int(input("B:"))
	ieq = int(i*a+(b*b)-b)
	print(ieq)
	print(type(ieq))
	
def floatcalc():
	x = float(input("X:"))
	y = 3.14
	z = 2.69
	feq = float(x+(y*z)+y)
	print(feq)
	print(type(feq))
	
def stringcat():
	str1 = "Hey now"
	str2 = "You're a"
	str3 = "Keemstar"
	str4 = "Do a trickshot"
	str5 = "MLG"
	stc = str1+str2+str3+str4+str5
	print(stc)
	print(type(stc))

def main():
		intcalc()
		floatcalc()
		stringcat()

main()
