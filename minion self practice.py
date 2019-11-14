s = input()
vowels = 'AEIOU'
count_kevin = 0
count_stuart = 0

for i in range(len(s)):
    if s[i] in vowels:
        count_kevin += (len(s) - i)
    else:
        count_stuart += (len(s) - i)


if count_kevin > count_stuart:
    print("Kevin", count_kevin)
elif count_stuart > count_kevin:
    print("Stuart", count_stuart)
else:
    pass





