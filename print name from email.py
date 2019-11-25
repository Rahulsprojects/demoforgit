'''s = input()
s = s.split("@")
print(s[0])'''

import re

emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2, emailAddress)
print(r2.group(1))
