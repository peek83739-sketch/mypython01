#โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
	#กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"
	#กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"
	#กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"
	#กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior"
	#กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

print(			'โปรแกรมแสดงข้อความต้อนรับนักศึกษา'			)
print('--------------------------------------------------')
name = input('ป้อนชื่อ: ')
year = int(input('ป้อนชั้นปี: '))
print('--------------------------------------------------')

if year == 1:
    print('Welcome Freshman','คุณ', name)
elif year == 2:
    print('Welcome Sophomore','คุณ', name)
elif year == 3:
    print('Welcome Junior','คุณ', name)
elif year == 4:
    print('Welcome Senior','คุณ', name)
else:
    print('Oh, no ...')