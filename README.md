This repository contains two implementations of searching for a set of strings in a base string. For each search string, all locations 
of the search string in the base string are printed.

The first program (substring1.py) is a simple implementation that uses the Python "find" method of strings.

The second program (substring2.py) first pre-processes the base string and creates an index - a dictionary mapping each character in
the base string to a list of positions where it occurs. This allows each search for a substring to start only at positions where the 
first character of the search string appears. A solution that pre-processes the base string and creates an index is better when the 
base string is long and many search strings are queried against it.
