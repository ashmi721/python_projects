'''Create a function that checks if two given strings are anagrams of each other. Anagrams are words or phrases
 formed by rearranging the letters of another.
'''
def check_anagrams(word1,word2):
    # remove the spaces and convert to lowercase
    word1 = word1.replace("","").lower()
    word2 = word2.replace("","").lower()

    # check the lengths are same or not
    if len(word1)!= len(word2):
        return False
    
     # Create dictionaries to count letter occurrences
    letter_count1 = {}
    letter_count2 = {}
    
     # Count occurrences of letters in word1
    for letter in word1:
        if letter in letter_count1:
            letter_count1[letter] += 1
        else:
            letter_count1[letter] = 1
     # Count occurrences of letters in word2
    for letter in word2:
        if letter in letter_count2:
            letter_count2[letter] += 1
        else:
            letter_count2[letter] = 1
    
     # Compare the dictionaries
    return letter_count1 == letter_count2

user_input1 = input("Enter the word1:")
user_input2 = input("Enter the word2:")

print(check_anagrams(user_input1,user_input2))