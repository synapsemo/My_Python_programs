def is_number_palindrome(num):
    if num < 0:
        return False  # Negative numbers are never palindromes
    
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10
        
    return original == reversed_num

print(is_number_palindrome(12321)) # True
print(is_number_palindrome(-121))  # False


# def is_palindrome(text):
#     return text == text[::-1]

# print(is_palindrome("madam"))  # True
# print(is_palindrome("python")) # False



# def is_phrase_palindrome(text):
#     cleaned = "".join(char.lower() for char in text if char.isalnum())
#     return cleaned == cleaned[::-1]

# print(is_phrase_palindrome("A man, a plan, a canal: Panama")) # True
