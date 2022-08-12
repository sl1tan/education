def isPalindrome(str):
    b = str.replace(" ", "")
    return b == b[::-1]


print(isPalindrome("nurses run"))
