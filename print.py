# name = "Анна"
# age = 25
# city = "Москва"
# hobby = "рисование"
print("Анна 25 Москва рисование")
print("Анна","25", "Москва", "рисование", sep= " ")
print("Анна","25", "Москва", "рисование", sep= ", ")
print("Анна","25", "Москва", "рисование", sep= "\n")
print("Анна, 25 лет, живёт в Москве, любит рисование.")
print("*" * 18)
print("*Анна",end="            *")
print("\n*25",end="              *")
print("\n*Москва",end="          *")
print("\n*рисование", end="       *")
print("\n" + "*" * 18)
print("\n")
print("Яблоко", "Груша", "Вишня", sep= " ")
print("Яблоко", "Груша", "Вишня", sep= "-")
print("Яблоко", "Груша", "Вишня", sep= ", ")
print("Яблоко", "Груша", "Вишня", sep= "/")
print("\n")
print("Имя: Иван","Телефон: 123-456-789","Email: ivan@mail.ru", sep="\n" )
print("\n")
print("*","**","***","****","*****",sep="\n")
print("\n")
print("****","*  *","*  *","****",sep="\n")
print("\n")
print("  * "," *** ","*****"," *** ","  * ",sep="\n")
print("  *  ", " *** ", "*****", " *** ", "  *  ", sep="\n")

name = input("Напиши чё-то")
print(name)

name ="alise"
age = 25
print(name, age)

name1, age1 = "Никита", 24
print(name1, age1)
name = "Артём"
age = 25
height = 145.65
is_student = True
print(name, age, height, is_student, sep=' ')
country, sity, language = "Russia", "sT. Petesburg", "Python"
print(country, sity, language)
balance = 1000
print("old " ,balance)
balance = 1500
print("new ",balance)
first_name = "Ivan"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)
a = 13
b =43
print(a, b, a*b, a+b)
print(type(a), type(b), type(a*b), type(a+b))
a = 3.14
b = 223
print(a*b)


#** - возведение в степень
#// - целое деление
#% - остаток
a = 4521.45
b = 5
c = float(b)
z = int(a)
print(a+b, a*b, a**b)
print(z)

a = 4521.45
p = round(a)
b = 5
c = float(b)
z = int(a)
print(a+b, a*b, a**b, round(a))
print(z)

number = input("Введи номер квартиры: ")
print("Подъезд: ")

print( (int(number)-1) //20 + 1)


print( (int(number)-1) % 20 // 4 + 1)

x = 10
y = 10
is_equal = (x==y)
print(is_equal)
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>5 and x< 11)
print(x == 0 or x == 5)

a = 10
print(a)
a = "hello"
print(a)



x = int(input("напиши число для password_count: \n"))
y = int(input("напиши число для y: \n"))
if x > 0 and y > 0:
    print("password_count and y are positive")
elif x < 0 and y < 0:
    print("password_count and y are negative")
else:
    print("something wrong")
message = "    "
if message:
    print("message")

    year = int(input("Введите год: \n"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("год високостный!")
    else:
        print("Обычный год")

        my_string = "hello world"
        my_string2 = 'hello world'
        my_text = """ 🎯 Твой исходный код абсолютно рабочий и правильный!
        Отличная работа! Ты правильно понял логику високосных лет и реализовал её на Python. 👏

        Теперь можешь усложнить задачу - например, сделать проверку на отрицательные годы или добавить цикл для многократной проверки! 🚀
        """
        print(my_text, "\n", my_string2, "\n", my_string, "\n")

        print(len(my_text))
        my_int = 100
        my_string8 = str(my_int)
        print(type(my_int), type(my_string8))
        big_int = 2 ** 1000
        bb = str(big_int)
        length = len(bb)
        print(length)
        big_int = int(bb)
        print("hello" in my_string)
        print(my_string2.upper())
        print(my_string2.lower())
        my_string = '                   H e l l o         world               '
        print(my_string)
        print(my_string.strip())
        print(my_string.count('o'))
        print(my_string.replace('H e l l o', 'Bye'))
        print(my_string.isdigit())
        name = "Alice"
        age = 25
        print(f"Hello, my name is {name} and my age is {age}")
        from time import process_time

        name = "Анна"
        age = 25
        print("Меня зовут {} и мне {} лет".format(name, age))
        name = "Аня"
        age = 21
        print("{1} {0}".format(name, age))
        print("{name} {age}".format(name="гоша", age=45))
        pi = 3.14159
        print("Число Пи: {:.6f}".format(pi))  # 2 знака после запятой
        # Вывод: Число Пи: 3.14
        print("{:<1}".format("левый"))  # Выравнивание по левому краю
        print("{:>20}".format("правый"))  # Выравнивание по правому краю
        print("{:^10}".format("центр"))  # Выравнивание по центру
        # Вывод:
        # левый
        #      правый
        #   центр
        number = 42
        print("{:050d}".format(number))  # 5 цифр с ведущими нулями
        # Вывод: 00042
my_list = [3,4,4,4,44,4,4,4,4,32323232323232,4,4,4,4,41213,2,32,31,4,41,24,3,5,5,6,6,6,2,7,7,88,331,9,9,0,3232131,34,3]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_string = "hello my name is Anton"
my_list22 = []
my_list22 = my_string.split(" ")
print(my_list22)

joined_string = my_list22

joined_string = " ".join(my_list22)
print(joined_string)

my_list = {1, 2, 33,2 ,4, 5 , 6, 6, 6,}
print(max(my_list))
print(min(my_list))
fruits = ["apple", "banana", "cherry", "watermelon", "mango"]
print(fruits)
print(fruits[0])
fruits[0], fruits[1] = fruits[1], fruits[0]
print(fruits)
numbers = [1, 2, 2,3,4,5,6,7,1]
print(numbers[0:len(numbers)])
print(numbers[:len(numbers)])
print(numbers[:])
print(numbers[0:len(numbers):5])
numbers = [1, 2, 2,3,4,5,6,7,1]
print(numbers[0:len(numbers)])
print(numbers[:len(numbers)])
print(numbers[:])
print(numbers[0:len(numbers):5])
print(numbers[0:5:1])
print(numbers[::-1])
file_names = ["kirill", "yor", "masha", "york", 5, 45.4]
print(file_names)


for name in file_names:
    print(name, type(name))
    gr = "Hello world!"
    count = 0
    for chars in gr:
        if "o" in chars:
            count += 1
            print(chars)
    print(count)
gr = "Hello world!"
count = 0
for chars in gr:
    if "o" in chars:
        count += 1
        print(chars)
print(count)
students = ["Alice", "Morgan", "Bob", "John", 'David']


for student in students:
    print(student)
    for char in student:
        print(char)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 1, 3, 5, 6, 33, 45, 1, 5, 2, 5]
for num in num:
    if num % 2 != 0:
        continue
    print(num)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 1, 3, 5, 6, 33, 45, 1, 5, 2, 5]
for num in num:
    if num  == 0:
        break
    print(num)
num = range(10)
print(num )
num = list(num)
print(num)
r = 2
print(type(num[0]))
nums = range(10,100,10)
print(list(nums))

gr = "Hello world!"
index = []
count = 0

for i in range(len(gr)):
    print(gr[i])
    if gr[i] == "o":
        index.append(i)
        count += 1

print(index)
print(count)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(len(number)):
    number[i] += 1
print(number)

number = 0
for i in range(1,11):
    number += i
    print(f"Добавляем {i}: сумма чисел: {number}")

fruits = ["яблоко", "лимон", "апельсин", "арбуз", "клубника"]
for i in fruits:
    print(f"Фрукт: {i}")

numbers = list(range(1,11))
print(numbers)
for i in range(len(numbers)):
    if numbers[i] % 2 !=0:
        continue
    print(numbers[i])

text = """ 
ПЕРЧАТКА
Перед своим зверинцем,
С баронами, с наследным принцем,
Король Франциск сидел;
С высокого балкона он глядел
На поприще, сраженья ожидая;
За королем, обворожая
Цветущей прелестию взгляд,
Придворных дам являлся пышный ряд."""
number_of_letter = 0
numbers_of_words = len(text.split())
numbers_of_sentence = 0
for letter in text:
    if letter != " " and letter != "\n":
        number_of_letter += 1
    if letter == "!" or letter == "?" or letter == "…" or letter == ".":
        numbers_of_sentence += 1

print("Подсчёт")
print("="*40)
print(f'Букв: {number_of_letter} Слов: {numbers_of_words}  Предложений: {numbers_of_sentence}')
print("="*40)

print("Таблица умножения на 5")
print("=" * 20)
for i in range(1, 11):
    print(f"5 * {i} = {5 * i}")
print("=" * 20)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 4 ,5, 6, 7, 2 ,5]
numbers5 = []
for i in range (len(numbers)):
    if numbers[i] > 5:
        numbers5.append(numbers[i])
print(numbers5)

numbers = [1, 2, 4 ,5 ,6, 7, 8, 44, 41,4 ,5 ,6 ,7, 6 , 8, 8, 3, 3,2, 3, 24, 3,46, 7,334]
max_number = 0
for i in range(len(numbers)):
    if numbers[i] > max_number:
        max_number  = numbers[i]
print("=" * 40)
print("Максимальное число найдено!")
print(f"максимальное число из списка = {max_number}")
print("=" * 40)

word = str(input("Введите слово:\n"))
shift = int(input("Введите число сдвига:\n"))
cesar_word = ""
print("Шифруем как Цезарь...")
print("=" * 20)
for i in word:
    cesar_word += chr(ord(i)+shift)
print(cesar_word)
print("=" * 20)

import random
import string

import random
import string

print("Добро пожаловать в генератор пароля!")
print("По умолчанию используются только буквы в нижнем регистре")
print("-" * 60)
password_len = int(input("Какая длина вашего пароля?\n"))

password_count = int(input("сколько паролей?\n"))

use_upcase = input("Хотите использовать заглавные буквы y/n?\n")
use_digit = input("Хотите использовать цифры y/n?\n")
use_punctuation = input("Хотите использовать спец. символы y/n?\n")

chars = (string.ascii_lowercase)
if use_upcase == "y":
    chars += string.ascii_uppercase
if use_digit == "y":
    chars += string.digits
if use_punctuation == "y":
    chars += string.punctuation
for i in range(password_count):
    password = ""
    for j in range(password_len):
        password += random.choice(chars)
    print("="*100)
    print("Пароль готов!")
    print(password)
print("="*100)

marks = [2, 2, 2, 4,4,4,4,4,4,5,5,5,1,2,3,4,5,3,3,3,3,5,5]
five_count = 0
summa = 0
four_count = marks.count(4)
for i in marks:
    if i == 5:
       five_count += 1
for i in range(len(marks)):
    summa += marks[i]
middle_mark = summa / len(marks)
print("Анализ твоих оценок!")
print("="*100)
print(f"Средняя оценка: {middle_mark}")
print(f"Количество пятерок: {five_count}")
print(f"Количество четвёрок: {four_count}")
print("="*100)

print("Поиск простых чисел от 2 до 20")
print("="*100)
simple_numbers = []
for i in range (2,21):
    print(i)
    is_go = True
    for j in range (2,i):
        if i % j == 0:
            is_go = False
            break
    if is_go == True:
        simple_numbers.append(i)
print("="*100)
print("Простые числа:")
print(simple_numbers)
print("="*100)

my_string = ""
for i in range(10):
    my_string += "*"
    print(my_string)

import time
my_word = ""
for i in "HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE.":
    my_word += i
    print(my_word)
    time.sleep(0.05)
print("Расчёт суммы")
print("=" * 30)
count_summa = int(input("Сколько вы хотите сложить чисел?\n"))
summa = 0
for i in range(count_summa):
    number =  int(input("Введите ваше число:\n"))
    summa += number
print(f"Ваша сумма: {summa}")
print("=" * 30)

word = "Программирование"
used_letters = []

for letter in word:
    if letter not in used_letters:
        count = 0
        for i in word:
            if letter == i:
             count += 1
        used_letters.append(letter)
        print(f"Буква {letter}: {count}")

numbers = [1, 4, 6 ,7, 2761, 8, 9, 5, 3, 44, 6, 5,  7,5,6,5,5,5,4,3,3,3,32,2,2,22,2,2,2,12,2,22,33,3,38,694]
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            number = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = number



print(numbers)

numbers_1 = [1,2 ,4 ,5 ,3,6232, 1,2,5,5]
numbers_2 = [1,148 ,698 ,5 ,3,22, 1,2,5,5]

def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average

average1 = find_average(numbers_1)
print(average1)
print(find_average(numbers_2))

def count_vowels(string):
    VOWELS = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    return count
print(count_vowels("""Hello world! HATE. LET ME TELL
YOU HOW MUCH I’VE
COME TO HATE YOU
SINCE I BEGAN TO
LIVE"""))
def function():
    pass
def function_1():
    print("Я НИЧЁ НЕ ДЕЛАЮ")
function_1()
def format_data(day: int, month: str):
    return f"this is {day} of {month}"

print(format_data(day=1, month = 'January'))

def format_data1(*, day: int, month: str) -> str:
    return f"this is {day} of {month}"
def greetings(*, name: str, gr: str = "Hello") -> str:
    return f"{gr} {name}"
print(greetings(name = "Victor"))
