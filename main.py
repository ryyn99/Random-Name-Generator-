import random

good_word= ["vision", "project", "operation", "network",
            "error", "apex", "umbrella", "connection", "alt",
            "function", "data", "format", "underground", "code", "cadaver"
            "protocol", "cyber", "parasite", "virus", "recursive", "ocean"]

try:
    numword = int(input('How many words do you want? '))
except ValueError:
    numword = 3

try:
    numnum = int(input('How many numbers do you want? '))
except ValueError:
    numnum = 3

random.shuffle(good_word)

book_name = good_word[0:numword]

for i in range(0, numnum):
    ran = random.randint(0, 100)
    book_name.append(str(ran))

final_name = ' '.join(book_name)
final_final= str.title(final_name)
print(f'Your suggested book name is {final_final}')
