""""
# 1.รับค่า text จากผู้ใช้
# 2.รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3.แสดงผลจำนวนของอักขระในข้อความ text 

# ตัวอย่างหน้าจอ
# Insert your text: Khanisorn Ketkeaw
# Character to find: o
# 5 letters 'o' found in 'Khanisorn Ketkeaw'



print("\n=== TRAVERSING STRINGS ===")
count = 0
text = input("Insert your text:")
char = input("Character to find:")

for letters in text:
    if letters == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")
"""



"""
# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า 8 ตัว , มีอักขระ @ 1 ตัว , มีตัวเลข , มีตัวอักษร
# 
# ตัวอย่างหน้าจอ
# Insert your password: khanisorn
# Your password in not storng!
#
# Insert your password: was@132
# Your password in not storng

password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum ()
    right = words[1].isalnum()

else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password is strog!") 
else:
    print("Your password in not storng!")
"""




