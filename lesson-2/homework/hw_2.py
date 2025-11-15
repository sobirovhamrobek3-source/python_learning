txt = 'LMaasleitbtui'
a = txt[0::2]
b = txt[-2::-2]
b=b[::-1]
print(a, b)
txt = 'MsaatmiazD'
a =txt[0::2]
b = txt[-1::-2]
print(a, b)
txt = "I'am John. I am from London"
parts = txt.split('from')
city =parts[1].strip()
print(city) 
name = "hamrobek"
name[::-1]
numbers = 1, 2, 3, 4, 5
maximum = max(numbers)
print("the maximum number is:", maximum)
word = input("hamrobek ")

if word == word[::-1]:
    print(word, "palindrom so'z")
else:
    print(word, "palindrom so'z emas")
  email = input("Email manzilingizni kiriting: ")
domain = email.split('@')[1]
print("Sizning domeningiz:", domain)
import random
import string
lenght = 8
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(lenght))
print("Yangi parolingiz:", password)
name = input("enter a name:" )
birth_year = int(input("enter your birth year: "))
current_year = 2025
age = current_year - birth_year
print("ismi",name)
print('tugilgan yili', birth_year)
print('yoshi',age)

text = input("Matn kiriting: ")

vowels = "aeiouAEIOU"   
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Unli harflar soni:", count)











