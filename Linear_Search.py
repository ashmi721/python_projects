def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return 1
    return -1

element = input("Enter the element of the tne list (space-separated):").split()
my_list = [int(a) for a in element]

target = int(input("Enter the element to search for: "))
index = linear_search(my_list,target)

if index != -1:
     print(f"Element {target} found in index {index}")
else:
    print(f"Element {target} not found in the list " )     