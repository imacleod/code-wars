def expanded_form(num):
    arr = sorted([(idx, val) for idx, val in enumerate(str(num)[::-1])], reverse=True)
    return ' + '.join(['{}'.format(val+'0'*idx) for idx, val in arr if val != '0'])


def expanded_form_2(num):
    num = str(num)
    final_str = ''
    for idx, val in enumerate(num):
        if val != '0':
            final_str += ' + {}{}'.format(val, (len(num[idx + 1:]) * '0'))
    return final_str.strip(' +')


def expanded_form_3(num):
    result = []
    for a in range(len(str(num))-1, -1, -1):
        current = 10 ** a
        quo, num = divmod(num, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)


print(expanded_form(10305))
print(expanded_form_2(10305))
print(expanded_form_3(10305))
