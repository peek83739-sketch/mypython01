# 3. on parameter have return
'''
det func_name( ) :
    คำสั่ง
    คำสั่ง
    .....
    return ค่าที่ต้องการส่งกลับ (ส่งค่ากลับไปที่จุดใช้ฟังก์ชั่น)
'''

def showHello( ):
    print('*_*')
    print('Wow')
    return 'Hello...'

def funcA ( ):
    print('Hi')
    return '*-*' , 10

print(showHello())

data = showHello( )
print(data)

inofor01, info02 = funcA( )
print(inofor01)
print(info02)