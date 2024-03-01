from collections import deque

def palindrome(text):
    text = text.lower()
    dequeN = deque()

    for symbol in text:

        if symbol.isalpha():
            dequeN.append(symbol)

    dequeR = deque(reversed(dequeN))

    print(dequeN, dequeR)

    return True if dequeN == dequeR else False
        
text1 = (input("Write string: "))
text2 = (input("Write string: "))
print(palindrome(text1), palindrome(text2))