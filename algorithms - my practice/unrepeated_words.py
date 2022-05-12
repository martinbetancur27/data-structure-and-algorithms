#Remove duplicates from a chain
print("\nRemove duplicates from a chain")

string = "dfnkdjsnfdskfndknsnk"
string_not_repeat = ""
repeated_word_switch = False

for i in range(0, len(string)):
    for j in range(i-1, -1, -1):
        if string[i] == string[j]:
            repeated_word_switch = True
    if not repeated_word_switch:
        string_not_repeat += string[i]
    repeated_word_switch = False

print(string + "\nno repeated words: " + string_not_repeat)

#Number of words that are not repeated in both strings

print("Number of words that are not repeated in both strings")

string_1 = "addaddffffddddddddddbcccccccccccd"
string_2 = "eeeeeeeeef1eeeeeeeeeeefgggaaaaaaaaaaagggggggg"
string_union = string_1 + string_2
repeated_word_switch = False

count_differents = 0

for i in range(0, len(string_union)):
    for j in range(i-1, -1, -1):
        if string_union[i] == string_union[j]:
            repeated_word_switch = True
    if not repeated_word_switch:
        count_differents += 1
    repeated_word_switch = False

print("Number of words that are not repeated: " + str(count_differents))

