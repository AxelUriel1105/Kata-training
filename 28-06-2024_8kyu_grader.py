"""Create a function that takes a number as an argument and returns a grade based on that number.

Score	Grade
Anything greater than 1 or less than 0.6	"F"
0.9 or greater	"A"
0.8 or greater	"B"
0.7 or greater	"C"
0.6 or greater	"D"
Examples:

grader(0)   should be "F"
grader(1.1) should be "F"
grader(0.9) should be "A"
grader(0.8) should be "B"
grader(0.7) should be "C"
grader(0.6) should be "D"
"""
def grader(score):
    return {score > 1 or score < 0.6: 'F',
            score >= 0.9 and score <= 1: 'A',
            score >= 0.8 and score < 0.9: 'B',
            score >= 0.7 and score < 0.8: 'C',
            score >= 0.6 and score < 0.7: 'D'
    }.get(True)
