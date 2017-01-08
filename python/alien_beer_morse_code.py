"""
The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply the
exact number of beers demanded. Unfortunately, the aliens only speak Morse code. Write a program to convert morse code
into numbers using the following convention:

1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----
"""
from re import findall

MORSE_TO_NUM = {
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
}


def morse_converter(string):
    return int(''.join(MORSE_TO_NUM[string[idx:idx+5]] for idx in range(0, len(string), 5)))


def morse_converter_2(string):
    alphabet = '1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----'.split()
    translator = dict(zip(alphabet[1::2], alphabet[::2]))
    answer = ''
    for val in findall('.{5}', string):
        answer = answer + translator[val]
    return int(answer)


print(morse_converter(".----"))
print(morse_converter("..----------..."))
print(morse_converter("----.--.....---...--"))

print(morse_converter_2(".----"))
print(morse_converter_2("..----------..."))
print(morse_converter_2("----.--.....---...--"))
