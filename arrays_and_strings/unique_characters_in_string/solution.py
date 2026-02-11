'''
Implement an algorithm to determine if a string has all unique characters. 
What if you can not use additional data structures?
'''

def isUniqueCharsString(s):
    '''
    in: string
    out: bool 
    '''

    # Approach 1: Brute Force
    # -----------------------
    # length = len(s)
    # for i in range(length):
    #     for j in range(i + 1, length):
    #         if s[i] == s[j]:
    #             return False
    # return True

    # Approach 2: Use a dictionary to store already occured chars
    # -----------------------------------------------------------
    # chars = {}
    # for ch in s:
    #     if ch not in chars:
    #         chars[ch] = True
    #     else:
    #         return False
    # return True

    # Approach 3: Using constant size array
    # -------------------------------------
    # Assumption: strings contain lowercase characters
    value = [1 for i in range(26)]
    base = 97
    for ch in s:
        pos = ord(ch) - base
        if value[pos] == 0:
            return False
        else:
            value[pos] = 0
    return True


def main():
    '''
    driver function
    '''
    s1 = 'abcdef'
    s2 = 'abcdefe'
    if isUniqueCharsString(s1):
        print('Pass for', s1)
    else:
        print('Failed for', s1)
    if not isUniqueCharsString(s2):
        print('Passed for', s2)
    else:
        print('Failed for', s2)


main()
