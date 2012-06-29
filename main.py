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

# main function
def main():
    c = raw_input(PROMPT).decode(INPUT_ENCODING)
    pb(c)
    pe(c, 'iso-2022-jp')
    pe(c, 'shift_jis')
    pe(c, 'utf-8')
    pe(c, 'utf-16')

# bootstrap
if __name__ == '__main__':
    main()
