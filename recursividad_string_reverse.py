'''De mi autoria'''
def stringReverse(word,size):
    
    size -= 1
    if(size == 0):
        print(word[size])
        return word[size]
    else:
        print(word[size])
        return word[size] + stringReverse(word, size)

'''Comentarios'''
def reverse_string2(string):
    if not string:
        return string
    print(string[1:] + string[0])
    return reverse_string2(string[1:]) + string[0]   

if __name__ == '__main__':
    word = str(input("Ingrese una palabra: "))
    
    size = len(word)
    string_reverse = stringReverse(word,size)
    #print(word)
    print(string_reverse)
    print("\n")
    print(reverse_string2(word))
 