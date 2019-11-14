def merge_the_tools(s, k):
    split_len = k
    lst = []
    new_lst = []
    for i in range(0, len(s), split_len):
        lst.append(s[i: (i + split_len)])
    for j in lst:
        for l in j:
            if l not in new_lst:
                new_lst.append(l)
        print("".join(new_lst))
        new_lst = []


if __name__ == '__main__':
    s, k = input(), int(input())
    merge_the_tools(s, k)
