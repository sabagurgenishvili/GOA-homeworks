
#def greet(name):
#    print(f"Hello {name}")

#greet("Data")

#def greet(name):
#    print(f"Hello {name}")

#print(greet("Data"))

# pass - გამოტოვება
# break - გაჩერება, დასტოპება, შეწყვეტა
# continue - 

def my_func(academy):
    if academy == "GOA":
        return "GOA is best"
    else: 
        pass
academy1 = input("Enter the best academy: ")
print(my_func(academy1))

#3) შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე, დააბრუნეთ სია სადაც იქნება ეს ჯამები ჩასმული, შესატანი მონაცემები [1,2,3,4,5] ---- გამოსატანი მონაცემები [6, 9] (edited)
#[8:49 PM]
# num % 2 == 0
# num % 2 != 0
even_list = []
odd_list = []

def summ(listn):
    for i in listn:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    sum_even = sum(even_list)
    sum_odd = sum(odd_list)
    return [sum_even, sum_odd]
          


print(summ([1,2,3,4,5]))
print(summ([1,2,3,4,5,6,7,8,9,10]))

def joinn(listn):
    sentence = ""
    for i in listn:
        sentence += i == " "
    return sentence

print(joinn(["Goal", "Oriented", "Academy"]))

#GoalOarientedAcademy
# Goal Oriented Academy

# python aris keysensetiv ena (amowmebs patara da did asoebs(lowercase and uppercase))