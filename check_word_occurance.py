'''Create a program that reads a text file, counts the occurrences of each word, 
and displays the most common words along with their frequencies.
'''
word_count = {}
with open("datas.txt",'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1

            else:
                word_count[word] -= 1  

for word, count in word_count.items():
    print(f'{word}: {count}')                  