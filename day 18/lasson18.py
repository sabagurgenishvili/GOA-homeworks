
#შექმენით ფუნქცია, რომელშიც გააერთიანებთ იმ ფუნქციებს რაც დღეს ვისწავლეთ (lower(), upper(), capitalize(), find())

#word = "GEGA"
#print(word.lower())

'''def func(string_list):
    index = input("Please enter index between 0" + "-" + str(len(string_list) - 1) + ": ")

    string_list[index] = "Luka
    
    result = "-".join(string_list)

    return result

print(func(["Luka", "Lile", "Nia"]))'''

def my_join(string_list, join_char):
    result = ''
    for word in string_list:
        result = result + word + join_char
    return result[0:-1]

print(my_join(["Luka", "Lile", "Nia"], "-"))


