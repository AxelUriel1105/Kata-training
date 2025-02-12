"""This is related to my other Kata about cats and dogs.

Kata Task
I have a cat and a dog which I got as kitten / puppy.

I forget when that was, but I do know their current ages as catYears and dogYears.

Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

NOTES:

Results are truncated whole numbers of "human" years
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""
def owned_cat_and_dog(cat_years, dog_years):
    owned_cat, owned_dog = years(cat_years, 'cat'), years(dog_years, 'dog')
    print(cat_years, dog_years)
    return [owned_cat,owned_dog]

def years(age, race):
    human_years = 0
    if age >= 15:
        human_years += 1
    age -= 15
    if age >= 9:
        human_years+=1
    age-=9
    if age >=5 and race == 'dog':
        human_years+= age//5
    if age >= 4 and race == 'cat':
        human_years+= age//4
    return human_years