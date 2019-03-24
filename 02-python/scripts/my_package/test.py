# from motivate import motivate_me, kick_ass, kick_up_the_backside

from motivate import *

try:
    motivate_me()
    kick_ass()
    kick_up_the_backside()
    daily_abuse()
except Exception as error:
    print(error)