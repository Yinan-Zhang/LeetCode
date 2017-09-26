def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    num = 0
    neg = 1
    idx = 0
    str = str.strip()
    for c in str:
        if c == "+" and idx == 0:
            neg = 1
            idx += 1
            continue;
        elif c == "-" and idx == 0:
            neg = -1
            idx += 1
            continue;
        if ord(c) in range(48,58):
            num = num * 10 + (ord(c)-48)
        else:
            return num*neg
        idx += 1

    num = num*neg
    if num > INT_MAX: return INT_MAX
    elif num < INT_MIN: return INT_MIN
    return num;


def test():
    cases    = ["", "fdasgdsa","123", "123456", "2147483648", "+1234", "-1234", "-2147483648"]
    expected = [0,0,123,123456, 2147483647, 1234,-1234, -2147483648];

    for i in range(len(cases)):
        if myAtoi(cases[i]) != expected[i]:
            print "Error on", cases[i], "\tExpecting:", expected[i], "\tGot:",myAtoi(cases[i]);

test()
