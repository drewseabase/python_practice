string_input = input("Enter a string ")
second_string = input("Enter another string ")

first_string_length = len(string_input)
second_string_length = len(second_string)
calc_start = first_string_length - second_string_length

if first_string_length >= second_string_length:
    slicing_first = string_input[calc_start::]
    print(slicing_first)

    if slicing_first == second_string:
        print(True)
    else:
        print(False)
else:
    print(False)

