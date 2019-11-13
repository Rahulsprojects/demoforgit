def minion_game(s):
    consnt = []
    vowel = ['a', 'e', 'i', 'o', 'u']
    count_kevin = 0
    count_stuart = 0
    for i in s:
        if i in vowel:
            vowel.remove(i)
            count_kevin += s.count(i)
            new_s = s[(s.find(i)):]
            for n in range(2, len(new_s) + 1):
                pos = 0
                while True:
                    pos = new_s.find(new_s[0:n], pos)
                    if pos > -1:
                        count_kevin += 1
                        pos += 1
                    else:
                        break
    for j in s:
        vowel = ['a', 'e', 'i', 'o', 'u']
        if j not in vowel:
            if j not in consnt:
                consnt.append(j)
                count_stuart += s.count(j)
                new_cs = s[(s.find(j)):]
                for k in range(2, len(new_cs) + 1):
                    new_pos = 0
                    while True:
                        new_pos = new_cs.find(new_cs[0:k], new_pos)
                        if new_pos > -1:
                            count_stuart += 1
                            new_pos += 1
                        else:
                            break
    if count_stuart > count_kevin:
        print('Stuart', count_stuart)
    elif count_kevin > count_stuart:
        print('Kevin', count_kevin)
    else:
        pass


if __name__ == '__main__':
    s = input()
    minion_game(s)
