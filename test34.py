#สร้างโปรแกรมคำนวณอายุของจากปีเกิด (พ.ศ.) ของพนักงานโรงงานแห่งหนึ่ง
#โดยป้อนชื่อและปีเกิดทางแป้นพิมพ์ ทั้งนี้โปรแกรมจะหยุดทำงานก็ต่อเมื่อป้อนชื่อพนักงาน เป็น SAU ก็จะหยุดทำงาน

#เขียนให้อยู่ในรูปแบบฟังก์ชัน จำนวน 4 แบบ

def show_program_name():
    print('   โปรแกรมคํานวณอายุพนักงาน    ')
def input_data():
    emp_name = input('ป้อนชื่อพนักงาน: ')
    if emp_name.upper() == 'SAU' :
        return emp_name, 0
    emp_year = int(input('ป้อนปีเกิด (พ.ศ.): '))
    return emp_name, emp_year

def calculate_age(emp_year):
    return (emp_year.now().year +543)- emp_year 

def print_result(emp_name, emp_year):   
    print(f'คุณ {emp_name} เกิดปี {emp_year} อายุ {print_result} ปี')

def check_sau(emp_name, emp_year):
    if emp_name.upper() == 'SAU' :
        print_result(emp_name, emp_year, 'จบการทำงาน')
    else:
        print_result(emp_name, emp_year, 'ทำงานต่อไป')
def show_pa():
    print('---------------------')
show_pa()
show_program_name()
show_pa()
emp_name, emp_year = input_data()
show_pa()
print_result(emp_name, emp_year)
show_pa()