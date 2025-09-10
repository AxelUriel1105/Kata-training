"""Write a pair of functions that convert from ASCII to hexadecimal and the other way around.

To make the conversion well defined, each ASCII character is represented by exactly two hex digits, left-padding with a 0 if needed.

The conversion from ascii to hex should produce lowercase strings (i.e. f6 instead of F6).

Example
ascii to hex: "Look mom, no hands" => "4c6f6f6b206d6f6d2c206e6f2068616e6473"

hex to ascii: "4c6f6f6b206d6f6d2c206e6f2068616e6473" => "Look mom, no hands"
"""
class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join(chr(int(h[i:i+2],16)) for i in range(0,len(h),2))
    
    @staticmethod
    def to_hex(s):
        return ''.join(hex(ord(c))[2::] for c in s)