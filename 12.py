lst = [1, 2, 2, 3, 4, 4, 5]    #removing duplicates from list
new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("After removing duplicates:", new_list)
