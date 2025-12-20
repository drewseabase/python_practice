def is_palindrome(s):
    a = s.lower()
    i, j = 0, len(a) - 1
    palindrome = True

    while i < j:
        if a[i] != a[j]:
            palindrome = False
            break
        i += 1
        j -= 1

    if palindrome:
        print("Is palindrome")
    else:
        print("Isn't palindrome")

s = input("Enter a string: ")
is_palindrome(s)