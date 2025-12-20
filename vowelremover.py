phrase = input("Enter a phrase: ")
vowels = 'a,e,i,o,u'.split(',')
new_phrase = ""

for i in phrase:
    if i  not in vowels:
        new_phrase += i
print(new_phrase)
