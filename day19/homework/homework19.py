word =(input("please enter your name: "))
reversed_word = ""

for index in range(len(word) - 1, -1, -1):
    reversed_word = reversed_word + word[index]

if word == reversed_word:
    print(word, "არის პალინდრომი")
else:
    print(word, "არ არის პალინდრომი")