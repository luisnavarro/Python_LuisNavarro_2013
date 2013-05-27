Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'abcdefg\tabc\ta'
print s
print len(s)
t = s.expandtabs()
print t
print len(t)
>>> 
abcdefg abc     a
13
abcdefg abc     a
17
