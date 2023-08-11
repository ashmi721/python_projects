'''"consecutive" means that two identical numbers appear one after the other in the list without any other number in between. So,
 when we say "two consecutive ones'''

def count_consecutive_ones(lst):
    count = 0
    total = 0
    prev_num = None
    consecutive_sequence = []
    for num in lst:
        if num == prev_num:
            count+= 1
            consecutive_sequence.append(num)
            if count == 2:
                 total+=1
                 print("Consecutive ones found:", consecutive_sequence)
        else:
            count = 1
            consecutive_sequence = [num]
        prev_num = num    
    return total    
elements = input("Enter the element of the list (space-separated): ").split()
my_list = [int(i) for i in elements]

result = count_consecutive_ones(my_list)
print("Occurences of two consecutive ones: ",result)
                
