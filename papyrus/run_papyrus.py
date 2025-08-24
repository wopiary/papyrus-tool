import webbrowser
import time
import os
import random
import logo_animation as module_animate
from curses import wrapper

def main():
    module_animate.wave_art(delay=0.05)
    def prGold(s): print("\033[38;5;220m {}\033[00m".format(s)) 
    def prTurquoise(s): print("\033[38;5;44m {}\033[00m".format(s)) 
    def prClayRed(s): print("\033[38;5;160m {}\033[00m".format(s))  
    def prVeryLightYellow(s): print("\033[38;5;229m {}\033[00m".format(s))
    def prCoyoteBrown(s): print("\033[38;2;125;91;63m {}\033[0m".format(s))   

    prVeryLightYellow("\nLiber scriptum est. Et scientia? Sit libera. ")       
    prGold("\n [1] Start Program")
    prTurquoise("[2] Settings")
    prClayRed("[3] Exit Program")
    print("\n\033[38;2;125;91;63m➤ Select Option: \033[0m", end='')
    user_input = input()
    match user_input:
        case '1':
            print('unrolling...')
        case '2':
            exit()
        case _:
            main()
    
main()

