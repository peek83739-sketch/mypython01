# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
print("===========================================")
print("โปรแกรมคำนวณผลรวมและค่าเฉลี่ยของจำนวนเต็ม 5 จำนวน")
print("===========================================")
number1 = int(input("ป้อนเลขตัวที่ 1: "))
number2 = int(input("ป้อนเลขตัวที่ 2: "))
number3 = int(input("ป้อนเลขตัวที่ 3: "))
number4 = int(input("ป้อนเลขตัวที่ 4: "))
number5 = int(input("ป้อนเลขตัวที่ 5: "))
sum_of_numbers = number1 + number2 + number3 + number4 + number5
average_of_numbers = sum_of_numbers / 5
print("===========================================")
print(f"ผลรวมของเลข 5 จำนวนคือ: {sum_of_numbers}")
print(f"ค่าเฉลี่ยของเลข 5 จำนวนคือ: {average_of_numbers}")
print("===========================================")

print('ผลรวม คือ:', sum_of_5_number)
print('ค่าเฉลี่ย คือ:', average_of_5_number)
print('===========================================')
print('ผลรวม คือ:' + str(sum_of_5_number))
print('ค่าเฉลี่ย คือ:' + str(average_of_5_number))
print('===========================================')
print('ผลรวม คือ: {}'.format(sum_of_5_number))
print('ค่าเฉลี่ย คือ: {}'.format(average_of_5_number))
print('===========================================')