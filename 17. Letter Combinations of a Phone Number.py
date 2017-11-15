
kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

def letterCombinations(digits):
    if digits is None or len(digits) == 0: return [];

    if len(digits) == 1 and digits in kvmaps:
        return [char for char in kvmaps[digits]];
    elif len(digits) == 1 and digits not in kvmaps:
        return [];
    elif len(digits) > 1:
        if digits[-1] in kvmaps:
            one_less_digit = letterCombinations(digits[:-1]);
            result = [];
            for comb in one_less_digit:
                for char in kvmaps[digits[-1]]:
                    result.append(comb+char)
            return result;
        return [];


print letterCombinations("23")
