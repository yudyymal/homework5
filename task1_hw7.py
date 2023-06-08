# text = "пара-ра-рам рам-пам-папам па-ра-па-да"
text = input("Введите стихотворение: ")
phrases = text.split()
vowels_count = []
for phrase in phrases:
    vowels = 0
    for letter in phrase:
        if letter.lower() in "ёуеыаоэяию":
            vowels += 1
    vowels_count.append(vowels)
if len(set(vowels_count)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")