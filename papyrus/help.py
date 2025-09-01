import os, time
LIGHT_SAND = "\033[38;2;237;201;175m"
SANDY_BROWN = "\033[38;2;210;180;140m"
TERRA_COTTA = "\033[38;2;204;102;51m"
CLAY_BROWN = "\033[38;2;181;101;71m"
SUNSET_GLOW = "\033[38;2;255;153;102m"
COYOTE_BROWN = "\033[38;2;125;91;63m"
RESET = "\033[0m"

def help_info():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"{LIGHT_SAND}Papyrus{RESET} is a tool that helps you find literature, also known as digital {SUNSET_GLOW}“scribes”{RESET} or {SANDY_BROWN}“papyrus”{RESET}, scattered across the vast {CLAY_BROWN}interwebs{RESET}.")
    print(f"Think of it as your personal librarian, scouring the web for knowledge and bringing it back to you in one place.\n")

    print(f"{TERRA_COTTA}1   Launch Papyrus.{RESET}")
    print(f"{COYOTE_BROWN}2   Enter your query for literature or “scribes.”{RESET}")
    print(f"{SUNSET_GLOW}3   Papyrus searches the interwebs for relevant digital scrolls.{RESET}")
    print(f"{SANDY_BROWN}4   Browse, save, or export the collected works.{RESET}\n")

    while True:
        user_input = input(f"{CLAY_BROWN}[e]{SUNSET_GLOW} to{CLAY_BROWN} Exit:{RESET} ").strip().lower()
        if user_input == 'e':
            return 'back'
        else:
            print(f"{TERRA_COTTA}Invalid input, staying in the current menu.{RESET}")



