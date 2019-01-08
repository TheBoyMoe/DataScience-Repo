b = ''
j_str = '''John Lennon. Witty, cheeky, sassy. You like
 to be the leader of your own band.'''
p_str = '''Paul McCartney. You are popular, likable, and
 charismatic. You make a great impression.'''
g_str = '''George Harrison. You are serious,reflective,
 and deeply committed to your work.'''
p_str = '''Ringo Starr. You are lovable and just want
 everyone to get along.'''

def main():
    a = ask_q('Are you more Assertive or Supportive? ', 'AS')
    if a == 'A':
        are_assertive()
    else:
        are_supportive()
    print('You are a', b)  # Global b assumed.

def are_assertive():
    global b
    a = ask_q('Are you more Intellectual or Social? ', 'IS')
    if a == 'I':
        b = j_str
    else:
        b = p_str
        
def are_supportive():
    global b
    a = ask_q('Are you more Intellectual or Social? ', 'IS')
    if a == 'I':
        b = g_str
    else:
        b = r_str

# Ask Q (question) function.
# This function takes a prompt message and a set of
# acceptable choices. Will re-prompt until user gives
# one of the choices... First letter, either case, is
# accepted.
def ask_q(msg, choices):
    while True:
        s = input(msg)
        s = s.upper()   # convert input to uppercase
        if s and s[0] in choices:
            return s[0]
        else:
            print('Enter one of the choices.')
            print('First letter is sufficient.')

main()
