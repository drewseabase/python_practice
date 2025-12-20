def is_pangram(st):
    letters = set()

    for ch in st.lower():
        if ch.isalpha():
            letters.add(ch)

    return len(letters) == 26

st = input()
is_pangram(st)

if is_pangram(st):
    print('Pangram')
else:
    print("Not pangram")





