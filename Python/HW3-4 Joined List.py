#Join all odd numbers from first list, and all even numbers from second list in
#another variable called joined_list

first_lst = [1,5,6,4,3,7,5,4,6,7,8]
second_lst = [4,3,7,5,4,9,8,7,8,6,5]

joined_list = []
for x in first_lst:
    if x % 2 != 0:
        joined_list.append(x)
for y in second_lst:
    if y % 2 == 0:
        joined_list.append(y)