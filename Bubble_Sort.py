my_list = []
swapped_list = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = int(input("Enter a list element: ")) #you will choose float type if you prefer
    my_list.append(val)

while swapped_list:
    swapped_list = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped_list = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
