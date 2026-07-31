# รับชื่อจริง (หรือข้อความ)จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว(a,e,i,o,u)


# ตัวอย่างหน้าจอ
# what is your name? : Khanisorn
# Your text have 4 vowel

name = input("What is your name? :  ")
letters = list("Khanisorn")
print(letters)

a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('i')
O = letters.count('O')
U = letters.count('U')

# Andy

count = 0
for letters in name : 
    if letters == 'a'or letters == 'A':
        count = count + 1 
    elif letters == 'e'or letters == 'E':
        count = count + 1 
    elif letters == 'i'or letters == 'I':
        count = count + 1 
    elif letters == 'o'or letters == 'O':
        count = count + 1 
    elif letters == 'u'or letters == 'U':
        count = count + 1
count = 0
for letters in name:     
    if letters in ['a','e','i','o','u','A','E','I','O','U']:
        count = count + 1
   
    #print(f"ตัวอักษร: {letters}")
#print("Your text have", count, "vowels")


