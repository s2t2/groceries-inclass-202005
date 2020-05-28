


my_numbers = [1, 2, 3, 4, 5, 6, 7]

print("ORIGINAL LIST", my_numbers)
#for i in my_numbers:
#    print(i)

#
# MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
#

new_numbers = []
for i in my_numbers:
    new_numbers.append(i * 100)
print("MAPPED LIST", new_numbers)

mapped_list = [i * 100 for i in my_numbers]
print("MAPPED LIST", mapped_list)

# FILTERED LIST : [4, 5, 6, 7]

filtered_list = []
for x in my_numbers:
    if x > 3:
        filtered_list.append(x)
print("FILTERED LIST :", filtered_list)

new_filtered_list = [x for x in my_numbers if x > 3]
print("FILTERED LIST :", new_filtered_list)
