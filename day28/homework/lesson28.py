def likes(names):
    if likes([]):
     print("no one like this")
    if likes("Peter"):
     print("Peter likes this")
    if likes(["Jacob", "Alex"]):
     print("Jacob and Alex like this")
    if likes(["Max", "John", "Mark"]):
     print("Max, John and Mark like this")
    if likes(["Alex", "Jacob", "Mark", "Max"]):
     print("Alex, Jacob and 2 others like this")
    return names