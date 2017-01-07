

def tail_swap(strings):
    first, second = strings[0].split(':'), strings[1].split(':')
    return ['{}:{}'.format(first[0], second[1]),
            '{}:{}'.format(second[0], first[1])]


print(tail_swap(['abc:123', 'cde:456']))
