# Substring Searching (version 1)
#
# This program takes a base string and a set of search strings. For
# each search string it returns all locations in the base string where
# the search string is a substring.
#
# This program is a simple implementation that uses the Python "find"
# method of strings. Each call to "find" in "find_substrings" returns
# the index of the next occurrence of the search string, or -1 if there
# isn't another occurrence.

base_str = None

# Find all occurrences of str1 in base_str using the find method
# of strings.
def find_substrings(str1):
    if base_str == None:
        print("Error: There is no base string")
        return
    
    found=False
    quote_str='"'+str1+'"'
    found_subs = list()

    pos=base_str.find(str1)
    while pos != -1:
        found_subs.append(pos)
        found=True
        pos=base_str.find(str1,pos+1)
        
    if found:
        if len(found_subs) > 1:
            print(quote_str, " found at positions", *found_subs)
        else:
            print(quote_str, " found at position", found_subs[0])
    else:
        print(quote_str, "is not a substring")

base_str="This is a test string for testing"
print("Base string is: ", base_str)
find_substrings("is")
find_substrings("test")
find_substrings("testing")
find_substrings(" ")
find_substrings("ing")
find_substrings("junk")

base_str="aaaaaaaaaaaaaaaaaaaaaaaaa"
print("Base string is: ", base_str)
find_substrings("aaa")
