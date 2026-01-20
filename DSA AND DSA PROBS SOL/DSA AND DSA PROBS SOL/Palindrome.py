def isPalindrome(str):
    reversedStr = str[::-1]
    if str == reversedStr:
        return True
    else:
        return False
    
print(isPalindrome("racecar"))  # True
print(isPalindrome("hello"))     # False