def isPalindrome(string):
    '''
    My Solution
    This is optimal
    O(n) runtime
    O(1) space
    '''
    l = len(string)
    first = 0
    last = l - 1
    while (first <= last):
        if string[first] == string[last]:
            first += 1
            last -= 1
        else:
            return False
    return True
