def palindrome(str):
    line = list(str.lower())
    line_reverse = list(str.lower())
    line_reverse.reverse()
    if line_reverse == line:
        return True
    else:
        return False


p1 = palindrome('оно')
p2 = palindrome('Луна')
p3 = palindrome('Шалаш')

print(p1, p2, p3)




