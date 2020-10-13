def check_polindrome(*args):
    backwards_nums = ''

    for number in args:
        for num in number:
            for char in num[::-1]:
                backwards_nums += char
            if num == backwards_nums:
                print(True)
            else:
                print(False)
            backwards_nums = ''


string = input().split(', ')
check_polindrome(string)
