

def hms(seconds):
    """ Return time as human-readable string HH:MM:SS """
    if not seconds:
        return '00:00:00'
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return '{:02}:{:02}:{:02}'.format(h, m, s)


if __name__ == "__main__":
    assert hms(0) == '00:00:00'
    assert hms(359999) == '99:59:59'
    print('Finished.')
