"""Let's create some scrolling text!

Your task is to complete the function which takes a string, and returns an array with all possible rotations of the given string, in uppercase.

Example
scrollingText("codewars") should return:

[ "CODEWARS",
  "ODEWARSC",
  "DEWARSCO",
  "EWARSCOD",
  "WARSCODE",
  "ARSCODEW"
  "RSCODEWA",
  "SCODEWAR" ]"""
def scrolling_text(text):
    scrolling_list = [text.upper()]
    for _ in range(len(text)-1):
        text = text[1::]+text[0]
        scrolling_list.append(text.upper())
    return scrolling_list