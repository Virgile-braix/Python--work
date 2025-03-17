# print("Hello Python")
# a = input("Enter the text you want : ")
# print( len(a) )

# a = input("Enter the message :")
# a = a.replace(" ", "")
# print(a)
# print(len(a))
ABC = []
for i in range(5):
    a = input(f"Enter the string you want {i + 1}: ")
    ABC.append(a.replace(" ",""))

for i, j in enumerate(ABC):
    print(f"The number of characters in string {i + 1} is {len(j)}")