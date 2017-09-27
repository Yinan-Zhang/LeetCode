def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """

    if numerator == 0: return "0";
    if denominator == 0: raise Exception("Denominator cannot be 0.")

    neg = False if (numerator<0 and denominator<0) or (numerator>0 and denominator>0) else True;
    numerator = abs(numerator)
    denominator = abs(denominator)

    rest = numerator;
    history = set([]);

    first_part = numerator / denominator;
    result = str(first_part);
    decimal_part = ""
    rest = numerator - denominator*first_part;

    while rest != 0:
        times10 = -1
        while rest < denominator:
            rest *= 10;
            times10+=1;
        if rest in history:
            temp = "0"*times10 + str(rest/denominator);
            idx = decimal_part.find(temp)
            decimal_part = decimal_part[0:idx] + "(" + decimal_part[idx:]
            decimal_part = decimal_part + ")";
            break;
        decimal_part += "0"*times10 + str(rest/denominator);
        if rest%denominator == 0:
            break;
        history.add(rest);
        rest = rest - rest/denominator * denominator

    if neg:
        result = "-"+result
    if len(decimal_part) > 0:
        return result + "." + decimal_part;
    else:
        return result;

def test():
    print fractionToDecimal(500, 10);

test()
