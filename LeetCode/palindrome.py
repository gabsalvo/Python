def isPalindrome(x):
    reverse_sum = 0
    original_x = x
    while x != 0 :
        last_digit = x % 10
        reverse_sum = reverse_sum * 10 + last_digit
        x = x//10
    print(reverse_sum)
    return print(reverse_sum == original_x)

isPalindrome(121)