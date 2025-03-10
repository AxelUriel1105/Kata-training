"""The snail crawls up the column. During the day it crawls up some distance. During the night she sleeps, so she slides down for some distance (less than crawls up during the day).

Your function takes three arguments:

The height of the column (meters)
The distance that the snail crawls during the day (meters)
The distance that the snail slides down during the night (meters)
Calculate number of day when the snail will reach the top of the column."""
def snail(column, day, night):
    days, distance = 0, 0
    while True:
        distance += day
        days+=1
        if distance >= column:
            return days
        distance-=night