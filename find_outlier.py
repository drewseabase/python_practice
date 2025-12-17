entered_string = input("Enter an series of numbers ")
split_string = entered_string.split()

highest = int(split_string[0])
lowest = int(split_string[0])

for i in split_string[1:]:
    num = int(i)
    if num >= highest:
        highest = num
    elif num <= lowest:
        lowest = num

print(f'{str(highest)} {str(lowest)}')





