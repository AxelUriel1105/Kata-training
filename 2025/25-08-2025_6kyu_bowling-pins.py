"""Mount the Bowling Pins!
Task:
Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:

I I I I  # each Pin has a Number:    7 8 9 10
 I I I                                4 5 6
  I I                                  2 3
   I                                    1
You will get an array of integers between 1 and 10, e.g. [3, 5, 9], and have to remove them from the field like this:

I I   I
 I   I
  I   
   I   
Return a string with the current field.

Note that:
The pins rows are separated by a newline (\n)
Each Line must be 7 chars long
Fill the missing pins with a space character ( )
Have fun!"""
def bowling_pins(arr : list[int]) -> str:
    bowling_pins = '7 8 9 x\n 4 5 6 \n  2 3  \n   1   '
    if 10 in arr:
        bowling_pins = bowling_pins.replace('x', ' ')
    for i in arr:
        bowling_pins = bowling_pins.replace(str(i),' ')
    print(bowling_pins)
    remove_bowling_pins = ''
    bowling_pins = bowling_pins.replace('10','1')
    for i in bowling_pins:
        if i.isdigit() or i == 'x':
            remove_bowling_pins += 'I'
        else:
            remove_bowling_pins += i
    return remove_bowling_pins
            