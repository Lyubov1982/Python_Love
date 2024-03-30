wordList = "Ежевику для ежат Принесли два ежа. Ежевику еле-еле Ежата возле ели съели."
e_words = 0

words = wordList.split()
for word in words:
    if word.lower().startswith('е'):
        e_words += 1

print("Количество слов на 'е': ", e_words)
