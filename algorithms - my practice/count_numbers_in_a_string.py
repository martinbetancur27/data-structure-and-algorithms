#Count how many numbers are in a string
print("\nCount how many numbers are in a string")

numbers = "0123456789"
string = "jf321skan2346mlm756845"
count_numbers = 0

for i in range(0, len(string)):
    for j in range(0, len(numbers)):
        if string[i] == numbers[j]:
            count_numbers += 1

print("String: " + string + "\nNumber of numbers: " + str(count_numbers))