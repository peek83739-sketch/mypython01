# 4.have parameter have return
'''
def func_name(parameter1, parameter2,...):
    คำสั่ง
    คำสั่ง 
    .....
    return ค่าที่ต้องการส่งกลับ (ส่งค่ากลับไปที่จุดใช้ฟังก์ชั่น)
'''

def funcA (n1,n2):
    print('Wow...')
    return n1 + n2

def funcB (data1, data2, data3):
    result = data1 * data2
    return result, data3 + result

print(funcA(10,20))

iot01 = funcA(5, 10)
print(iot01)

aa, bb = funcB(10, 20 ,30)
print(aa)   
print(bb)