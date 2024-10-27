"""Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values (oldest age first) if those exist or null/None or {-1, -1} in C if:

sum < 0
difference < 0
Either of the calculated ages come out to be negative
"""
def get_ages(sum_, difference):
    oldest, younger = ((sum_+difference)/2,(sum_-difference)/2)
    return None if sum_ < 0 or difference < 0 or oldest < 0 or younger < 0 else (oldest,younger)"""
