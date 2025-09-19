# คำสั่ง break, conitune
# break ใน loop ทำงานเมื่อใดจบ loop ทันที
# continue ใน loop ทำงานเมื่อใด จบ loop แค่รอบนั้นทันทีให้ไปรอบต่อไปเลย

for aa in range(5) :
    if aa == 2 :
        break
    print(aa, 'Hi...')

print('+++++++++++++++++')
for aa in range(5) :
    if aa == 2 :
        continue
    print(aa, 'Hi...."')