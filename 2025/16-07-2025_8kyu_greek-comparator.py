"""Write a comparator for a list of phonetic words for the letters of the greek alphabet.

A comparator is:

a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument

(source: https://docs.python.org/2/library/functions.html#sorted)

The greek alphabet is preloded for you as greek_alphabet:

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
Examples
greek_comparator('alpha', 'beta')   <  0
greek_comparator('psi', 'psi')      == 0
greek_comparator('upsilon', 'rho')  >  0"""
#from preloaded import greek_alphabet


def greek_comparator(lhs, rhs):
    if lhs==rhs: return 0
    greek_alphabet_dict = dict(zip(greek_alphabet,range(1,25)))
    print(greek_alphabet_dict)
    return 1 if greek_alphabet_dict[lhs] > greek_alphabet_dict[rhs] else -1
