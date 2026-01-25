def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    output_words = [ word[::-1] if len(word) >= 5 else word for word in words ]
    # for word in words:
    #     if len(word) >= 5:
    #         output_words.append(word[::-1])
    #     else:
    #         output_words.append(word)
    return " ".join(output_words)


# "Hey fellow warriors"  --> "Hey wollef sroirraw"
# "This is a test"        --> "This is a test"
# "This is another test" --> "This is rehtona test"

print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
