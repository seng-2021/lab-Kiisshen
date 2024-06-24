'''
Module for encoding and decoding in ROT13, but also chaning case of letters.
'''
import codecs

def encode(s):
    '''
    Encoding function that encodes in ROT13 but also changes lower case to upper case, 
    and upper case to lower case, as well as changes numbers to special characters.
    '''
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s = s.ljust(1000, 'a')
    for c in s:
        if c not in digitmapping:
            if ord(c.upper()) > 90 or ord(c.upper()) < 65:
                raise ValueError()
        if c.isalpha():
            if c.islower():
                c=c.upper()
            else:
                c=c.lower()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]

    return crypted[0:origlen]

def decode(s):
    '''
    Decoding Function for encoded strings using the same logic as the encoder.
    '''
    return encode(s)
