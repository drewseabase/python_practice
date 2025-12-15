pangram = input("Enter a phrase ").lower()
pangram_list = []
new_list=[]
previous_char = None
counter = 0
for i in pangram:
    if i.isalpha():
        pangram_list.append(i)
pangram_list.sort()

for i in pangram_list:
    if i != previous_char:
        new_list.append(i)
        previous_char = i
        counter +=1

if counter < 26:
    print(False)
else:
    print(True)






