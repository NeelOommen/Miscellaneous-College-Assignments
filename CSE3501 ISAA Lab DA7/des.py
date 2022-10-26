def hexToBin(inpStr):
    key = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    s = ""
    for  i in range(0, len(inpStr)):
        s += key[inpStr[i]]
    
    return s


def binToHex(inpStr):
    key = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }

    new_str = ''

    i = 0
    while i < len(inpStr):
        temp_str = inpStr[i:i+4]
        new_str += key[temp_str]
        i += 4
    
    return new_str
    


def initialPermutation(inpStr):
    ip = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
    61,33,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

    per_str = ""
    for i in range(0, len(inpStr)):
        per_str += inpStr[ip[i] - 1]

    return (per_str[0:32], per_str[32:64])


def reduceKey(inpStr):
    new_key = ""

    for i in range(0, len(inpStr)):
        if(i>0 and i%8 != 0):
            new_key += inpStr[i]

    return new_key


def shiftCircular(key):
    return key[1:len(key)] + key[0]


def reduceTo48Bits(key, round):
    round_shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    halfOne = key[0:28]
    halfTwo = key[28:56]

    r = round_shift[round]

    while r>0:
        halfOne = shiftCircular(halfOne)
        halfTwo = shiftCircular(halfTwo)
        r-=1

    mask = [14,17,11,24,1,5,3,28,15,6,21,10,
    23,19,12,4,26,8,16,7,27,20,13,2,
    41,52,31,37,47,55,30,40,51,45,33,48,
    44,49,39,56,34,53,46,42,50,36,29,32]

    temp_key = halfOne + halfTwo

    new_str = ""

    for i in range(0, len(mask)):
        new_str += temp_key[mask[i] - 1]

    return new_str


def expandTo48Bit(inpStr):
    exp_map = [32,1,2,3,4,5,4,5,
    6,7,8,9,8,9,10,11,
    12,13,12,13,14,15,16,17,
    16,17,18,19,20,21,20,21,
    22,23,24,25,24,25,26,27,
    28,29,28,29,30,31,32,1]

    new_str = ""

    for i in range(0, len(exp_map)):
        new_str += inpStr[exp_map[i] - 1]

    return new_str


def bitwiseXOR(text, key):
    new_str = ""

    for i in range(0, len(text)):
        new_str += ('1' if (text[i] == key[i]) else '0')

    return new_str

    
def finalPermutation(inpStr):
    perm_map = [40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25]

    per_str = ""
    for i in range(0, len(perm_map)):
        per_str += inpStr[perm_map[i] - 1]

    return per_str


plain_text = '12345ABCD1325368'
cipher_key = 'AABC398134ABEEF1'

#implement steps of algorithm
bin = hexToBin(plain_text)

lStr, rStr = initialPermutation(bin)

#key transformation
key56bit = reduceKey(hexToBin(cipher_key))

for i in range(0,16):
    #key transformation
    key48bit = reduceTo48Bits(key56bit,i)

    #expansion permutation
    expanded_l = expandTo48Bit(lStr)
    expanded_r = expandTo48Bit(rStr)

    #xor halves with key
    lStr = bitwiseXOR(expanded_l, key48bit)
    rStr = bitwiseXOR(expanded_r, key48bit)

combined_string = lStr + rStr

cipher_text = finalPermutation(combined_string)

print(f'The final generated cipher text is {cipher_text} (length of {len(cipher_text)} bits) or {binToHex(cipher_text)}')