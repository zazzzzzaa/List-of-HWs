word_inp = input("Введите слово на проверку палиндрома: ")
# word_check = word_inp[::-1]
# if word_check == word_inp:
#     print(f"слово {word_inp} является палиндромом!")
# else:
#     print(f"Слово {word_inp} НЕ является палиндромом")

def pal(word: str) :
    word_check = word[::-1]
    if  word_check.lower() == word.lower():
        return True
    else:
        return False
print(pal(word_inp))