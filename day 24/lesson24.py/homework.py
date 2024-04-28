#თქვენ მუშაობთ რიცხვების სიაზე, შესაძლოა გქონდეთ როგორც მთელი რიცხვები, ასევე ათწილადები. დავალებაა, რომ დააბრუნოთ სიის რიცხვების ჯამი, მაგრამ  ამ ჯამში არ შევა მაქსიმალური და მინიმალური მნიშვნელობები.

# num = [3 , 5 , 7.3 , 4.1]

# sum = 0
# for i in num:
#     ty = type(i)
#     if ty == int:
#         sum = i + sum
# print(sum)


#ლებაა, რომ დააბრუნოთ სიის რიცხვების ჯამი, მაგრამ  ამ ჯამში არ შევა მაქსიმალური და მინიმალური მნიშვნელობები.

# num = int(input(" pls enter an num: "))
# nums = []
# for i in range (1 , num+1):
#     if num % i == 0:
#         nums.append (i)
# print (nums)

 # 8 kyu
#1
def litres(time):
    return (time * 0.5) // 1

#2
def paperwork(n, m):
    if n  < 0 or m < 0:
        return 0
    else:
        return n * m

#3
def grow(arr):
    ans = 1
    for i in arr:
        ans = i
    return ans

#4
def fake_bin(x):
    new_str = ""
    for i in x:
        if int(i) < 5:
            new_str += "0"
        else:
            new_str += "1"
    return new_str

#5
def count_by(x, n):
    new_list = []
    for i in range(1, n + 1):
        new_list.append(i x)
    return new_list
[3:41 PM]
#7 kyu
#1
def to_jaden_case(string):
    splited_string = string.split()
    new_list = []
    for i in splited_string:
        i = i.capitalize()
        new_list.append(i)

    return " ".join(new_list)

#2
def accum(st):
    new_list = []
    new_list2 = []
    new_list3 = []
    for i in st:
        new_list.append(i)

    for j in range(len(new_list)):
        new_list2.append(new_list[j] * (j + 1))

    for z in new_list2:
        new_list3.append(z.capitalize())
    return "-".join(new_list3)


#3
def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        min = numbers[0]
        for i in numbers:
            if min > i:
                min = i
        numbers.remove(min)
        return numbers
#6 kyu
#1
def solution(number):
    result = 0
    if number <= 0:
        return 0
    else:
        for i in range(1, number):
            if i % 3 == 0 or i % 5 == 0:
                result += i
        return result

#2
def likes(names):
    if names == []:
        return "no one likes this"
    else:
        for i in names:
            if len(names) == 1:
                return f"{i} likes this"
            elif len(names) == 2:
                return f"{names[0]} and {names[1]} like this"
            elif len(names) == 3:
                return f"{names[0]}, {names[1]} and {names[2]} like this"
            elif len(names) > 3:
                return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


