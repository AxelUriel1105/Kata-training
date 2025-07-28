"""Implement String#ipv4_address?, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc."""
import re
def ipv4_address(address):
    pattern = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
    try:
        ipv4_0, ipv4_1, ipv4_2, ipv4_3 = pattern.match(address).group(1),pattern.match(address).group(2),pattern.match(address).group(3),pattern.match(address).group(4)
        if '\n' in address: return False
        if ipv4_0 != str(int(ipv4_0)) or ipv4_1 != str(int(ipv4_1)) or ipv4_2 != str(int(ipv4_2)) or ipv4_3 != str(int(ipv4_3)):
            return False
        if 0 <= int(ipv4_0) <= 255 and 0 <= int(ipv4_1)<= 255 and 0 <= int(ipv4_2) <= 255 and 0 <= int(ipv4_3) <= 255:
            return True
        return False
    except: 
        return False