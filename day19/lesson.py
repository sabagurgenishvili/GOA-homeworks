'''string_list = []

for i in range(5):
    word = input("Please enter word: ")
    string_list.append(word)

join_char = input("Please enter char to join strings in list: ")

result = ""

for index in range(len(string_list)):
    if index % 2 == 0:
        result = result + string_list[index] + join_char

restult = result[:-1]

print(result)'''

join_char = input("Please enter char to join strings in list: ")
result = ""

for i in range(5):
    word = input("Please enter word: ")
    if i % 2 == 0:
        result = result + word + join_char

print(result[0:-1])
#_______________________________________

#მომხმარებელს შემოატანინეთ სიტყვა. for ციკლის გამოყენებით შეამოწმეთ მისი თითოეული ასო და თუ რომელიმე იქნება lowercase, მაშინ მომხმარებელს შემოატანინეთ სიტყვა თავიდან. ასევე დაბეჭდეთ თუ რამდენჯერ მოუწია მომხმარებელს სიტყვის შემოტანა - counter.
#char - სიმბოლო
user_word = input("Please enter uppercase word: ")

count = 1

for char in user_word:
    
    if char.lower() not in user_word:
        user_word = input("Please enter uppercase word: ")
        count = count + 1
         
print(count, user_word)

#მომხმარებელს შემოატანინეთ სიტყვა. თქვენი დავალებაა, რომ ლუწ ინდექსებზე მყოფი ასოები გარდაქმნათ uppercase-ად, ხოლო კენტ ინდექსებზე მყოფები lowecase-ად, საბოლოოდ კი დაბეჭდოთ შედეგი.
#len - რამდენი ელემენტია ცვლადში

user_word = input("Please enter uppercase word: ")

for index in range(len(user_word)):
    if index % 2 == 0:   
        result = result + user_word[index].upper()
    else: 
        result = result + user_word[index].lower()

print(result)    

#სიაში შეინახეთ თქვენი სახელი და გვარი. capitalize მეთოდის გამოყენებით მასივის ყველა ელემენტზე მოახდინეთ მუშაობა და ბოლოს დაბეჭდეთ უკვე შეცვლილი სია.

names = ["luka", "gio", "lile", "nia"]

for index in range(len(names)):
    names[index] = names[index].capitalize()

print(names)
#______________________________________

#მომხმარებელს შემოატანინეთ სახელი, შემდეგ კი გვარი. შეინახეთ ისინი სიაში და წინა დავალების მსგავსად იმუშავეთ ყველა ელემენტზე capitalize მეთოდით. თქვენი დავალებაა, რომ გამოიტანოთ მომხმარებლის ინიციალები სთრინგის სახით. test case: input) "Data", "Tezelashvili" -> output: "D.T"

firstname = input("Please enter your firstname: ").capitalize()
lastname = input("Please enter lastname: ")

result = firstname[0] + ',' + lastname[0]

print(result)
#______________________________________

#თქვენი დავალებაა, რომ შექმნათ იგივე ლოგიკა რაც წინა დავალებაში გქონდათ, უბრალოდ find მეთოდის გარეშე - გამოიყენეთ ციკლი. საბოლოოდ შეამოწმეთ ორივე ალგორითმის მუშაობა და შეამოწმეთ იგივე შედეგებს თუ მიიღებთ.

def manual_find(collection, find_item):
    for index in range(len(collection)):
        if collection[index] == find_item:
            return index
    return -1

print(manual_find("Luka", "x"))