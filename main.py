#!/usr/bin/env python2.6
# -*- encoding: utf-8 -*-
# vim: tw=0 ts=4 sw=4 sts=4 et

INPUT_ENCODING = 'utf-8'
PROMPT = 'str:'

# print as byte string
def pb(c):
    print "   ",
    for i in c:
        print hex(ord(i)),
    print

# print unicode string in specified encoding
def pe(c, enc):
    print enc
    try:
        pb(c.encode(enc))
    except UnicodeEncodeError, e:
        print e

def kuten(c):
    try:
        s = c.encode('euc-jp')
    except UnicodeEncodeError, e:
        print e
        return
    i = 0
    print "kuten"
    print "   ",
    while i < len(s):
        cp = ord(s[i])
        men = 1
        if cp == 0x8F:
            men = 2
            i = i + 1
            cp = ord(s[i])
        elif cp == 0x8E:
            # JIS X 0201 1byte char
            i = i + 1
        if cp > 0xA0:
            print "%d-%02d-%02d" % (men, ord(s[i]) - 0xA0, ord(s[i + 1]) - 0xA0),
            i = i + 1
        else:
            # ascii
            print ".",
        i = i + 1

# main function
def main():
    c = raw_input(PROMPT).decode(INPUT_ENCODING)
    pb(c)
    pe(c, 'iso-2022-jp')
    pe(c, 'shift_jis')
    pe(c, 'cp932')
    pe(c, 'euc-jp')
    pe(c, 'utf-8')
    pe(c, 'utf-16')
    kuten(c)

# bootstrap
if __name__ == '__main__':
    main()
