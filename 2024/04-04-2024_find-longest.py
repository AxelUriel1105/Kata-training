"""Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array."""
def find_longest(arr):
    return int(list(filter(lambda x: len(x) == len(str(sorted(arr)[-1])), map(str,arr)))[0])
