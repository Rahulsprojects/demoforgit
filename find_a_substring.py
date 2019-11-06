def count_substring(string, sub_string):
    value = 0
    for i in range(len(string)):
        if sub_string in string:
            index = string.find(sub_string)
            value += 1
            string = string[index + 1:]
    return value


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)