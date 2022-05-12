string = "heeellooo"

char = input("Enter character: ")
count_char = 0

for i in range(0, len(string)):
	if(string[i] == char):
		count_char += 1


print(char + "--> " + str(count_char) + " times")

#############################

chars = []

print("\n--- Count repeats of each character ---\n")
for i in range(0,len(string)):
    if (string[i] not in chars):
        chars.append(string[i])
        count_char = 1
        for j in range(i+1,len(string)):
            if (string[j] == chars[-1]):
                count_char += 1
        print(chars[-1] + "--> " + str(count_char) + " times")
