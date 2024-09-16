"""When we specify the number of fewer than 4, the result will be a specified number of strings; if the number of the partition is too many, the results will only be the same as the default results.

If we use the empty string as the separator, we'll get an array of strings containing each character:

var str="My name is John";
var words=str.split("");
console.log(words);

//output:
[ 'M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'J', 'o', 'h', 'n' ]
Split can use regular expressions to split the string. But because we have not learned the use of regular expressions, so we do not have to learn this usage.

concat() can merge many strings into a string like this:

var str="My".concat("name","is","John");
console.log(str);

//output:
MynameisJohn
In fact, we rarely see the actual use of concat(), because we have a more simple way. that is using the + operator:

var str="My"+"name"+"is"+"John";
console.log(str);

//output:
MynameisJohn
But even using the + operator, the four words are not the perfect combination of a sentence, because there is no space separator. What should we do? Using join() is the best choice.

join() is the reverse operation of the split() method. We can see a lot of code in the actual use:

var str="My name is John";
var words=str.split(" ");
console.log("use split():",words);
var s=words.join(" ");
console.log("use join():",s);
console.log("use split() and join():",str.split(" ").join(" "))
//output:
use split():[ 'My', 'name', 'is', 'John' ]
use join():My name is John
use split() and join():My name is John
Ok, lesson is over. let's us do some task.

Task
Implement a function which accepts 2 arguments: string and separator.

The expected algorithm: split the string into words by spaces, split each
 word into separate characters and join them back with the specified separator, join all the resulting "words" back into a sentence with spaces.

For example:

splitAndMerge("My name is John", " ")  ==  "M y n a m e i s J o h n"
splitAndMerge("My name is John", "-")  ==  "M-y n-a-m-e i-s J-o-h-n"
splitAndMerge("Hello World!", ".")     ==  "H.e.l.l.o W.o.r.l.d.!"
splitAndMerge("Hello World!", ",")     ==  "H,e,l,l,o W,o,r,l,"""
def split_and_merge(string_, separator):
    return ' '.join(f'{separator}'.join(w) for w in string_.split())