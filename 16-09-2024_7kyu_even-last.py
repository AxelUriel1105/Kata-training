"""Given a sequence of integers, return the sum of all the integers that have
 an even index (odd index in COBOL), multiplied by the integer at the last index.

Indices in sequence start from 0.

If the sequence is empty, you should return 0."""
def even_last(numbers): 
    print(numbers)
    return sum(n for i,n in enumerate(numbers) if i % 2 == 0)*numbers[-1] if numbers else 0