#Word counter in a string
print("\nWord counter in a string")
string = " One Two   Three Four is good  "
count_words = 0

if(len(string) > 0 and string != " "):

    #prevent counting leading white space
    if string[0] != " ":
        count_words += 1

    index_validator = 1 #validate that there are not two spaces in a row
    for i in range(0, len(string)):

        if string[i] == " " and  string[index_validator] != " ":
            count_words += 1

        if(index_validator < len(string)-1):
            index_validator += 1

print("Phrase: " + string + "\nNumber of words: " + str(count_words))