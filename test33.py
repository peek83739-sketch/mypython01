# โปรแกรมตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือ
# โดยหากค่าคาร์บอนไดซ์ออกไซน์มีค่าเกินกว่า 678.55 ให้แสดงข้อความว่า “ไม่ผ่าน”  หากน้อยกว่า 678.55
# ให้แสดงข้อความ “ผ่าน” โดยให้รับชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้ทางแป้นพิมพ์

# รับฃื่อเจ้าของรถ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้
# การตรวจสอบค่าคาร์บอนไดซ์ออกไซน์
# การแสดงผล
# แสดงฃ่ือโปรแกรม

def show_program_name():
    print('   ตรวจสอบสภาพรถ      ')
     
def input_data():
    car_owner = input('ป้อนชื่อเจ้าของรถ: ')
    car_number = input('ป้อนทะเบียนรถ: ')
    car_carbon = float ( input ('ป้อนปริมาณก๊าซคาร์บอนไดซ์ออกไซน์: '))
    return car_owner, car_number, car_carbon

def show_result(car_owner, car_number, car_carbon, result):
    print(f'คุณ {car_owner} รถทะเบียน {car_number} ')
    print(f'มีค่าคาร์บอนไดซ์ออกไซน์ {car_carbon} สรุป {result} ')
def check_gas(car_owner, car_number, car_carbon) :
    if car_carbon > 678.55:
        # ไม่ผ่านเกณฑ์
        show_result(car_owner, car_number,car_carbon, 'ไม่ผ่านเกณฑ์')
    else:
         # ผ่านเกณฑ์
         show_result(car_owner, car_number,car_carbon, 'ผ่านเกณฑ์')

def show_pa():
    print('---------------------')

show_pa()
show_program_name()
show_pa()
car_owner, car_number, car_carbon = input_data()
show_pa()
check_gas(car_owner, car_number, car_carbon)
show_pa()