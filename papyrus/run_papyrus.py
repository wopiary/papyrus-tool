import webbrowser
import time
import os
import random
import logo_animation as module_animate
from curses import wrapper
import papyrus_mainfile
import help

def main():
    os.system('cls' if os.name=='nt' else'clear')
    module_animate.wave_art(delay=0.05)

    gold = "\033[38;5;220m"
    very_light_yellow = "\033[38;5;229m"
    turquoise = "\033[38;5;44m"
    clay_red = "\033[38;5;160m"
    coyote_brown = "\033[38;2;125;91;63m"
    cactus_green = "\033[38;2;107;142;35m"
    golden_dune = "\033[38;2;218;165;105m"
    sahara_beige = "\033[38;2;244;196;153m"
    reset_color = "\033[0m"

    
    print(f"\n\n{very_light_yellow}Liber scriptum est. Et scientia? Sit libera{reset_color}")
    print(f"\n{sahara_beige}==========================================={reset_color}")
    print(f"{gold}[1] Start Program{reset_color}")
    print(f"{turquoise}[2] Settings{reset_color}")
    print(f"{clay_red}[3] ReadME{reset_color}")
    print(f"{coyote_brown}[4] Exit Program{reset_color}")
    print(f"{sahara_beige}==========================================={reset_color}")
    user_input = input(f"\n{cactus_green}➤ Select Option{reset_color} ")
    if len(user_input.strip()) == 0:
        main()

    match user_input:
        case '1':
            result = papyrus_mainfile.main()
        case '2':
            pass
        case '3':
            result = help.help_info()
            if result =='back':
                main()
        case '4':
            print(f"{golden_dune}Exiting...{reset_color}")
            exit()

            
    
main()
