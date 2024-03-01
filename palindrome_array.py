def palindrome(text):
    text = text.lower()
    arr = []

    for symbol in text:

        if symbol.isalpha():
            arr.append(symbol)

    arr_rev = arr[::-1]

    print(arr, arr_rev)
    if arr == arr_rev:
        return True
    else:
        return False

text1 = (input("Write string: "))
text2 = (input("Write string: "))
print(palindrome(text1), palindrome(text2))