# Substring Searching (version 2)
#
# This program takes a base string and a set of search strings. For
# each search string it returns all locations in the base string where
# the search string is a substring.
#
# This program first pre-processes the base string and creates an index -
# a dictionary mapping each character in the base string to a list of
# positions where it occurs.This allows each search for a substring to
# start only at positions where the first character of the search string
# appears.
#
# This solution is better when the base string is long (ex. the text of
# the Bible) and many (ex. millions) search strings will be queried
# against it. The index can contain all substrings of the base string
# from length 1 to m (say m=5) as keys.

start_pos = {}
base_str = None
base_len = 0

# Set up a dictionary of start locations for each character in the
# base string. Each unique character in base_str will have a list
# of positions where the character occurs.
def find_starts():
    if base_str == None:
        print("Error: There is no base string")
    else:
        print("Base string is: ", base_str)
        global base_len
        base_len=len(base_str)
        for i in range(base_len):
            ch=base_str[i] # Add i to start positions for ch
            if ch not in start_pos:
                start_pos[ch] = list()
            start_pos[ch].append(i)

# Find all occurrences of str1 in base_str using the dictionary
# start_pos for start positions for searching.
def find_substrings(str1):
    if base_str == None:
        print("Error: There is no base string")
        return
    
    found=False
    first=str1[0]
    quote_str='"'+str1+'"'
    found_subs = list()

    if first in start_pos: # Only search if first character is in base_str
        possible_subs=start_pos[first]
        str_len = len(str1)
        for i in possible_subs:
            if i+str_len <= base_len and str1 == base_str[i:i+str_len]:
                found_subs.append(i)
                found=True
    if found:
        if len(found_subs) > 1:
            print(quote_str, " found at positions", *found_subs)
        else:
            print(quote_str, " found at position", found_subs[0])
    else:
        print(quote_str, "is not a substring")

base_str="This is a test string for testing"
find_starts()
find_substrings("is")
find_substrings("test")
find_substrings("testing")
find_substrings(" ")
find_substrings("ing")
find_substrings("junk")

start_pos = {}
base_str="aaaaaaaaaaaaaaaaaaaaaaaaa"
find_starts()
find_substrings("aaa")
