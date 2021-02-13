from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    s = ""
    z = ""
    i = 1

    while i <= n:
        z = str(i)
        s += z
        i += 1

    print(s)