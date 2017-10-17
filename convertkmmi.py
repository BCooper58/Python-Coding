def print_menu():
	print('1. Kilometers to Miles')
	print('2. Miles to Kilometers')

def km_miles():
	km=float(input('ENTER KILOMETER DISTANCE:'))
	miles=km/1.609
	
	
	print('MILE DISTANCE: {0}'.format(miles))
	
def miles_km():
	miles=float(input('ENTER MILE DISTANCE:'))
	km=miles*1.609
	
	print('KILOMETER DISTANCE:{0}'.format(km))
	
if __name__ == '__main__':
	print_menu()
	choice=input('WHICH CONVERSION YOU WANT?:')
	if choice == '1':
		km_miles()
		
	if choice == '2':
		miles_km()

