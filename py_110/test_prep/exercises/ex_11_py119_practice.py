"""
Problem:  Create a function that finds a repeating pattern, if present, in a string.
    Input:  string
    Output:  tuple, with two elements of string and integer ( «substring» , «integer» )
    Rules
        Explicit
            - nonempty input string assumed
            - return string element and integer pair should maximize the integer component (count) and minimize the string substring_length
            - assume that the string argument consists entirely of lowercase alphabetic letters
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  

Algorithm
    - Create a dictionary with keys of all combinations of substrings that meet the condition of recurring being a pattern (recurring through the whole string), with values equal to how many times the substring occurs in the string
    - return the dictionary member with the highest count

Implementation by Code
    - 
"""
def pattern_count(string, substring):
    substring_length = len(substring)
    occurrences = string.count(substring)
    if substring_length*occurrences == len(string):
        return occurrences
    else:
        return 0

def repeated_substring(string):
    substring_counts = {}
    for index1 in range(len(string)):
        for index2 in range(index1, len(string)):
            substring = string[index1 : index2 + 1]
            substring_counts[substring] = pattern_count(string, substring)
    
    max_count = max(substring_counts.values())
    for pattern, occurrences in substring_counts.items():
        if occurrences == max_count:
            return (pattern, occurrences)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
