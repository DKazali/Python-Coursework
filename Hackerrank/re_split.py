# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = raw_input()
m = str(n)
i = re.search(r'([a-zA-Z0-9])\1+', m)
print(i.group(1) if i else -1)