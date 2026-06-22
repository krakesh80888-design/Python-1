def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()

    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("madam"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))