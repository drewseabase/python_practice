integer = int(input("Enter an int "))
binary = bin(integer)
binary_count = 0

for i in binary:
    if i == '1':
        binary_count+=1
print(binary_count)



