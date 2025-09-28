def rotate(text, key):
    # list all letters of the alphabet
    plain = "abcdefghijklmnopqrstuvwxyz"
    final=[]

    for char in text:
        # check if char is in alphabet
        if char in plain:
            char_index= plain.index(char)
            if char_index+key>25:
                char_index-=26
            final.append(plain[char_index+key])
        # check if char is in alphabet but uppercase
        elif char.lower() in plain:
            char_index= plain.index(char.lower())
            if char_index+key>25:
                char_index-=26
            final.append(plain[char_index+key].upper())
        # for any other character such as punctuation, leave it as is
        else:
            final.append(char)
    return "".join(final)

text= input("Enter text to translate: ")
key= input("Enter key: ")
print(rotate(text, int(key)))