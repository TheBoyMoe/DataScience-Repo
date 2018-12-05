"""
This is a multi-line STRING - IT IS NOT a COMMENT
open IDLE:  $ python3 -m idlelib.idle

This is a doc string for this file
Because the string is triple quoted it can
span multiple lines

>>> m = Markov('ab')
>>>m.predict('a')
'b'
"""
# dunder/magic method
# __init__ is the class constructor
# not req'd, default constructor provided if not defined
class Markov:
    # self is the instance of the class
    def __init__(self, data):
        pass
        # self.table = None

    def predict(self, data_in):
        return 'b'

def get_table(data):
    ''' This is a function docstring
    This will return a transition table
 
    >>> get_table('ab')
    {'a': {'b': 1}}
    '''
    results = {}   # dictionary literal
    # import pdb; pdb.set_trace()
    for i in range(len(data)):
        char = data[i]
        try:
            out = data[i+1]
        except IndexError:
            break
        if char in results:
           char_dict = results[char]
        else:
            char_dict = {}
        if out not in char_dict:
            char_dict[out] = 0
        char_dict[out] += 1
        results[char] = char_dict
    return results
 
# refactored version of get_table
def get_table_refactored(data):
    ''' This is a function docstring
    This will return a transition table
 
    >>> get_table('ab')
    {'a': {'b': 1}}
    '''
    results = {}   # dictionary literal
    for i, char in enumerate(data):
        try:
            out = data[i+1]
        except IndexError:
            break
        char_dict = results.get(char, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[char] = char_dict
    return results
 
              
# no need to provide args to constructor
class Test:
    def __init__(self):
        self.table = None

class TestTest:
    def __init__(self, a, b):
        self.table = None
