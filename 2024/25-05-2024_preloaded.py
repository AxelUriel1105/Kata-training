"""
You are using a library that already has the functions below. 
Create a function named main that calls the functions in the proper order.

- `combat`
- `buy_health`
- `get_coins`
- `print_status`
- `roll_dice`
- `move`"""
from preloaded import *

health = 100
position = 0
coins = 0

def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()
    