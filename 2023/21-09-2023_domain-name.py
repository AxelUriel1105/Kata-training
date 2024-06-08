"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"""
def domain_name(url):
    removeThis = ["http://","www.","https://"]
    if removeThis[0] in url:
        url = url.replace(removeThis[0],"")
    if removeThis[1] in url:
        url = url.replace(removeThis[1],"")
    if removeThis[2] in url:
        url = url.replace(removeThis[2],"")

    return url.split(".")[0] 