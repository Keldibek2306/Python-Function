def is_palindrome(text: str):
    return text == text[::-1]


print(is_palindrome("radar"))   
print(is_palindrome("hello"))    