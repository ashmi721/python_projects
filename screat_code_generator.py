# write a python program to translate a mesage into secret code language. Use the rules below to translate 
# normal english into secret code languag

# coding:
import random
user_input = input("Enter the message:")
words = user_input.split(" ")
secreat_word = []
for word in words:
   if len(word)>=3:
      rw = random.choices('abcdefghijklmnopqrstuvwxyz', k=3)
      new_word = ''.join(rw) + word[1:] + word[0] +''.join(rw)
      secreat_word.append(new_word)
   else:
     secreat_word.append(word[::-1])
print("Secret code:",' '.join(secreat_word))

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now the last letter 
secret_words = str(secreat_word).split(",")

normal_words = []

for secret_word in secret_words:
    if len(secret_word) >= 3:
        normal_word = secret_word[::-1]
        normal_words.append(normal_word)
    else:
      rw = secreat_word[3:-4]
      last_letter = secret_word[-1]
      normal_words.append(normal_word)
print("Normal code:",' '.join(normal_words))