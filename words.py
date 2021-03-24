

# Step 1-2

words = ['holiness', 'theology', 'sanctification', 'salvation']

def print_upper_words(list):
    new_list = [x.upper() for x in words]
    print(new_list)

print(print_upper_words(words))


# Step 3

def print_e_words(words):
    for word in words:
        if word[0] == 'e':
            print(word)
        else:
            print("Unqualified!")

print(print_e_words(['hello', 'elephant']))


# Step 4

def print_words_with_key_letters(words, key_letters):
    for word in words:
        if key_letters[0] in word or key_letters[1] in word:
            print(word)
        else:
            print("Not valid, kid!")

print(print_words_with_key_letters(['mind', 'child'], ['m', 'r']))

