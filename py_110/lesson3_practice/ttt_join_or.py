"""
Problem:  create a join_or function, similar to the list.join() method, that includes default positional arguments to specify a delimiter and final conjunction before the last item is listed.
    Input:  list, of values
    Output:  string, of delimited and concatenated values
    Rules
        Explicit
            - 
        Implicit
            - uses ', ' as the default delimiter
            - uses 'or ' as the default final conjunction (in addition to the delimiter when the number of values is greater than 2)
            - an empty input list produces an empty string as return value
    Questions
        - ()

Examples/ Test Cases
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

Data Structures:  

Algorithm
    - find length of input list
        + if the number of elements in the list is greater than 2, include delimiters
        + if the number of elements in the list is greater than 1, include the final conjunction
        + add concatenating string elements to every other item in a new (copied) list, according to rules
    - concatenate list

Implementation by Code
    - remember to convert element to string if they're not already.
"""
def join_or(lst, delimiter=', ', list_conjunction='or'):
    lst = [str(element) for element in lst]

    if len(lst) > 1:
        if len(lst) > 2:
            lst = [lst[i // 2] if i % 2 == 0 else delimiter for i in range(len(lst)*2)]
            lst.pop()
            lst.insert(-1, list_conjunction + ' ')
        else:
            lst.insert(-1, ' ' + list_conjunction + ' ')
    return ''.join(lst)

print(join_or([1, 2, 3]) == "1, 2, or 3")
print(join_or([1, 2, 3], '; ') == "1; 2; or 3")
print(join_or([1, 2, 3], ', ', 'and') == "1, 2, and 3")
print(join_or([]) == "")
print(join_or([5]) == "5")
print(join_or([1, 2]) == "1 or 2")