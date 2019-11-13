s = input()
for test_fun in [".isalnum", ".isalpha", ".isdigit", ".islower", ".isupper"]:
    print(any(eval("c" + test_fun + "()") for c in s))