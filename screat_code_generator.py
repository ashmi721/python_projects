# write a python program to translate a mesage into secret code language. Use the rules below to translate 
# normal english into secret code languag

# coding:
''' if the word contain more than 3 characters, than add random 3 word 
to start and last , NOw remove first letter to add before the random word
else:
 word contain less than 3 characters, reverse it
'''
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
'''if the word contains less than 3 characters, reverse it
else:
 remove 3 random characters from start and end. Now the last letter add first
'''
secret_words = ' '.join(secreat_word).split()  # Join the secret words and split them by spaces
normal_words = []

# Loop through each secret word
for secret_word in secret_words:
    if len(secret_word) <= 3:
        # If the secret word has 3 or fewer characters, reverse it to get the original word
        normal_word = secret_word[::-1]
        normal_words.append(normal_word)
    else:
        # Extract the last letter and characters between the 4th and 2nd-to-last letters
        last_letter = secret_word[-4]
        rw = secret_word[3:-4]

        # Reconstruct the original word
        normal_word = last_letter + rw
        normal_words.append(normal_word)

# Print the decoded message
print("Normal code:", ' '.join(normal_words))
