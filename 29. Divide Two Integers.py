import pdb

def helper(num, target):
    res = 0
    while True:
        print "\t",target, num
        if target == num:
            return res;
        elif target < num:
            return res-1
        num = num << 1;
        res +=1

def divide(dividend, divisor):


    neg = False if (dividend<0 and divisor<0) or (dividend>0 and divisor>0) else True;
    dividend = abs(dividend);
    divisor  = abs(divisor);

    if dividend == divisor: return -1 if neg else 1;

    res = 0;
    while True:
        print "--------------"
        print dividend, divisor
        if divisor == dividend:
            res += 1;
            break;
        if dividend < divisor:
            res = -res if neg else res
            break;
        two_pow = helper(divisor, dividend);
        print two_pow
        res += 2 ** two_pow
        dividend = dividend - (divisor<<two_pow);

    if res >= 2147483647:
        return 2147483647
    return res

def test():
    print divide(65,4);
    #print divide(2147483647,1);

test()
