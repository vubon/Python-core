'''
words = {
    0:'Zero',
    1 : 'One',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'}

tens = [
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

def number(num):
    if num < 100:
        return twodig(num[1:3])
    else:
       return ' '.join([ words[int(num[0])],  'hundred',  twodig(num[1:3]) ])

def twodig(num):
    if num <= 0:
        return words[num]
    else:
        return ''.join([tens[int(num[0]) - 1], '-', words[int(num[1])]]) '''

import sys

words = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen'
}

tens = [
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

placeholders = [
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion'
]

# segMag = segment magnitude (starting at 1)
def convertTrio(number):
    if int(number) < 100:
        return convertDuo(number[1:3])
    else:
        return ' '.join([ words[int(number[0])],  'hundred',  convertDuo(number[1:3]) ])


def convertDuo(number):
    #if teens or less
    if int(number[0]) <= 1:
        return words[int(number)]
    #twenty-five
    else:
        return ''.join([tens[int(number[0]) - 1], '-', words[int(number[1])]])

def num2words(numeral):
    numeral = str(numeral)
    if len(numeral) % 3:
        numeral = numeral.zfill( (3 - (len(numeral) % 3)) + len(numeral) )
    numeralSegments = [numeral[i-3:i] for i in range (len(numeral), 0, -3)]
    group_names = [convertTrio(seg)+' '+placeholders[i]
                   for (i,seg) in enumerate(numeralSegments)]
    group_names.reverse()
    return ', '.join(group_names)
    #return ', '.join(reversed(group_names))

def main(*args):
    return '\n'.join([num2words(number) for number in args])
    #return '\n'.join(num2words(number) for number in args)

if __name__ == "__main__":
    print(main(*(sys.argv[1:] or ('',))))