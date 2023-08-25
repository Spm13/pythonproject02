#รับค่า/ป้อนทางแป้นพิมพ์ input() สิ่งที่ป้อนเป็น string

#ตัวแปร variable เป็น identifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม ข้อมูลที่จะเก็บจะอยู่ใน RAM
#identifier คือ ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
print('-------------')
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
stdAge = 2023 - int(stdYearBorn)  #ต้องแปลง string เป็น number -> int( ), float( )
print(f"คุณเกิดปี {stdYearBorn} อายุ {stdAge}")