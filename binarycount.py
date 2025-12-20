def count_bits(n):
    binary = bin(n)
    binary_count = 0

    for i in binary:
        if i == '1':
            binary_count += 1
    print(binary_count)

n = int(input("Enter something: "))
count_bits(n)