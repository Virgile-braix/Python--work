# print("Hello Python")
# a = input("Enter the text you want : ")
# print( len(a) )

# a = input("Enter the message :")
# a = a.replace(" ", "")
# print(a)
# print(len(a))
# ABC = []
# for i in range(5):
#     a = input(f"Enter the string you want {i + 1}: ")
#     ABC.append(a.replace(" ",""))

# for i, j in enumerate(ABC):
#     print(f"The number of characters in string {i + 1} is {len(j)}")

def kajipotefu(text):
    # Create the transformation dictionary
    conversion_dict = {
        'k': 'a', 'a': 'k',
        'j': 'i', 'i': 'j',
        'p': 'o', 'o': 'p',
        't': 'e', 'e': 't',
        'f': 'u', 'u': 'f',
        'K': 'A', 'A': 'K',
        'J': 'I', 'I': 'J',
        'P': 'O', 'O': 'P',
        'T': 'E', 'E': 'T',
        'F': 'U', 'U': 'F'
    }

    # Convert the input string
   
    kajii = ""
    
    for char in text:
        kajii += conversion_dict.get(char, char)  # If char not in dict, keep it unchanged
    
    return kajii

# Test the function
u_input = input("Enter a string: ")
converted_str = kajipotefu(u_input)
print("converted string:", converted_str)