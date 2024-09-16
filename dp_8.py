def rev(s):
    words=s.split()
    words.reverse()
    return ' '.join(words)

s = input("Enter the string: ")
print(f"Reversed words: '{rev(s)}'")