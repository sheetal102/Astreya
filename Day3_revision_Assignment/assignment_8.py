string = input("Enter a string: ")

vowels = 0
consonants = 0

for letter in string:
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter.isalpha(): 
        consonants += 1

print(f"Vowels: {vowels}")        
print(f"Consonants: {consonants}")