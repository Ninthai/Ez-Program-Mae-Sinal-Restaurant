
import datetime
import pytz

bangkok_tz = pytz.timezone('Asia/Bangkok')
nowtime1 = datetime.datetime.now(bangkok_tz)
nowtime2 = nowtime1.strftime("%H:%M:%S")
count = 0
time = 0
ls = []
summ = 0

print('\nร้านอาหารตามสั่งแม่สีนาล')

print('\n--------------------------------------------------')

print('\nรายการอาหาร(อร่อยทุกอย่าง)')

print('1) ข้าวผัดกุ้ง (50 บาท)     2) ข้าวผัดไก่ (50 บาท)\n3) ข้าวผัดหมู (50 บาท)     4) ราดหน้า (60 บาท)\n5) ต้มยำกุ้ง (65 บาท)      6) ข้าวกระเพราหมูสับ (50 บาท)     \n7) Exit\n--------------------------------------------------')

while True:
    enterinput = int(input('\nกรุณากรอกเลขอาหารที่ต้องการ: '))
    if enterinput == 1:
        count += 50;time += 15;ls.append('ข้าวผัดกุ้ง')       
    elif enterinput == 2:
        count += 50;time += 15;ls.append('ข้าวผัดไก่')        
    elif enterinput == 3:
        count += 50;time += 15;ls.append('ข้าวผัดหมู')
    elif enterinput == 4:
        count += 60;time += 20;ls.append('ราดหน้า')        
    elif enterinput == 5:
        count += 65;time += 20;ls.append('ข้าวผัดหมู')
    elif enterinput == 6:
        count += 50;time += 10;ls.append('ข้าวกระเพราหมูสับ')        
    elif enterinput == 7:
        print(f'\nรายการอาหารของคุณคือ: {",".join(ls)}\nราคาอาหารของคุณคือ: {count} บาท\nเวลาตอนนี้คือ: {nowtime2}\nเวลาที่ต้องรอคือ {time} นาที')
        intin2 = input('โปรดกรอกว่ารายการของคุณถูกต้องหรือไม่(Yes/No): ')
        if intin2 == ('Yes') or intin2 == ('yes') or intin2 == ('YES') or intin2 == ('yEs') or intin2 == ('yeS'):
            intin1 = int(input('กรุณากรอกเงินของคุณ: '))
            if intin1 < count:
                print('ยอดเงินของคุณไม่พอ ทางร้านของอนุญาตถอดคำสั่งของคุณ')
                break
            elif intin1 >= count:
                print(f'เงินคงเหลือของคุณคือ: {abs(count - intin1)} บาท\nขอบคุณที่ใช้บริการร้านอาหารตามสั่งแม่สีนาล')
                break
        elif intin2 == ('No') or intin2 == ('nO') or intin2 == ('no') or intin2 == ('NO'):
            print('\nกรุณากรอกใหม่อีกรอบ')
            print('\n1) ข้าวผัดกุ้ง (50 บาท)     2) ข้าวผัดไก่ (50 บาท)\n3) ข้าวผัดหมู (50 บาท)     4) ราดหน้า (60 บาท)\n5) ต้มยำกุ้ง (65 บาท)      6) ข้าวกระเพราหมูสับ (50 บาท)     \n7) Exit\n--------------------------------------------------')
            count = 0;time = 0;summ = 0;ls = []
        else:
            print('\nกรุณากรอกใหม่อีกรอบ')
            print('\n1) ข้าวผัดกุ้ง (50 บาท)     2) ข้าวผัดไก่ (50 บาท)\n3) ข้าวผัดหมู (50 บาท)     4) ราดหน้า (60 บาท)\n5) ต้มยำกุ้ง (65 บาท)      6) ข้าวกระเพราหมูสับ (50 บาท)     \n7) Exit\n--------------------------------------------------') 
            count = 0;time = 0;summ = 0;ls = []                        
    else:
        print('\nกรุณากรอกใหม่')
        print('\n1) ข้าวผัดกุ้ง (50 บาท)     2) ข้าวผัดไก่ (50 บาท)\n3) ข้าวผัดหมู (50 บาท)     4) ราดหน้า (60 บาท)\n5) ต้มยำกุ้ง (65 บาท)      6) ข้าวกระเพราหมูสับ (50 บาท)     \n7) Exit\n--------------------------------------------------')
        count = 0;time = 0;summ = 0;ls = []