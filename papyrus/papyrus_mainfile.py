import webbrowser
import time
import os
from urllib.request import urlretrieve
import urllib
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cloudscraper
import requests
import sys

colors = {
    "gold": "\033[38;5;220m", "very_light_yellow": "\033[38;5;229m", "turquoise": "\033[38;5;44m", "clay_red": "\033[38;5;160m", "coyote_brown": "\033[38;2;125;91;63m", "cactus_green": "\033[38;2;107;142;35m", "golden_dune": "\033[38;2;218;165;105m", "sahara_beige": "\033[38;2;244;196;153m",
    "neon_oasis": "\033[38;2;0;255;200m", "neon_cactus": "\033[38;2;57;255;20m", "neon_sky": "\033[38;2;0;191;255m", "neon_dusk": "\033[38;2;138;43;226m", "neon_heatwave": "\033[38;2;255;94;0m", "neon_bloodmoon": "\033[38;2;255;36;0m", "neon_scorch": "\033[38;2;255;255;0m", "neon_flare": "\033[38;2;255;20;147m",
    "neon_starlight": "\033[38;2;0;255;255m", "neon_sandstorm": "\033[38;2;255;165;79m", "desert_rose": "\033[38;2;199;21;133m", "crimson_sunset": "\033[38;2;220;20;60m", "amber_glow": "\033[38;2;255;191;0m", "copper_flame": "\033[38;2;184;115;51m", "sage_whisper": "\033[38;2;159;175;166m", "ocean_depth": "\033[38;2;0;119;190m",
    "forest_shadow": "\033[38;2;34;139;34m", "midnight_blue": "\033[38;2;25;25;112m", "royal_purple": "\033[38;2;120;81;169m", "cherry_blossom": "\033[38;2;255;183;197m", "slate_storm": "\033[38;2;112;128;144m", "ivory_pearl": "\033[38;2;255;255;240m", "charcoal_smoke": "\033[38;2;54;69;79m", "rust_orange": "\033[38;2;183;65;14m",
    "lime_burst": "\033[38;2;50;205;50m", "magenta_shock": "\033[38;2;255;0;255m", "teal_wave": "\033[38;2;0;128;128m", "bronze_shield": "\033[38;2;205;127;50m", "lavender_mist": "\033[38;2;230;230;250m", "coral_reef": "\033[38;2;255;127;80m", "steel_gray": "\033[38;2;70;130;180m", "emerald_fire": "\033[38;2;80;200;120m",
    "plasma_pink": "\033[38;2;255;0;150m", "electric_blue": "\033[38;2;0;150;255m", "toxic_green": "\033[38;2;128;255;0m", "volcanic_red": "\033[38;2;255;69;0m", "arctic_white": "\033[38;2;248;248;255m", "deep_violet": "\033[38;2;148;0;211m", "solar_yellow": "\033[38;2;255;215;0m", "cyber_cyan": "\033[38;2;0;255;255m",
    "shadow_black": "\033[38;2;28;28;28m", "bone_white": "\033[38;2;245;245;220m", "wine_red": "\033[38;2;114;47;55m", "mint_fresh": "\033[38;2;152;251;152m", "storm_purple": "\033[38;2;75;0;130m", "flame_orange": "\033[38;2;255;140;0m", "ice_blue": "\033[38;2;176;224;230m", "earth_brown": "\033[38;2;139;69;19m",
    "neon_lime": "\033[38;2;191;255;0m", "neon_violet": "\033[38;2;148;0;255m", "neon_coral": "\033[38;2;255;114;118m", "neon_aqua": "\033[38;2;0;255;146m", "neon_gold": "\033[38;2;255;215;0m", "neon_crimson": "\033[38;2;255;20;60m", "neon_emerald": "\033[38;2;0;255;127m", "neon_sapphire": "\033[38;2;15;82;186m",
    "ghost_white": "\033[38;2;248;248;255m", "blood_orange": "\033[38;2;255;69;0m", "forest_green": "\033[38;2;34;139;34m", "sunset_orange": "\033[38;2;255;94;77m", "ocean_blue": "\033[38;2;0;105;148m", "rose_gold": "\033[38;2;183;110;121m", "silver_mist": "\033[38;2;192;192;192m", "jade_green": "\033[38;2;0;168;107m",
    "cosmic_purple": "\033[38;2;102;51;153m", "lava_red": "\033[38;2;207;16;32m", "thunder_gray": "\033[38;2;70;70;70m", "crystal_blue": "\033[38;2;173;216;230m", "golden_honey": "\033[38;2;255;185;15m", "velvet_red": "\033[38;2;144;12;63m", "pine_green": "\033[38;2;1;121;111m", "sand_beige": "\033[38;2;245;245;220m",
    "aurora_green": "\033[38;2;0;255;127m", "phoenix_orange": "\033[38;2;255;165;0m", "galaxy_purple": "\033[38;2;75;0;130m", "pearl_white": "\033[38;2;240;234;214m", "obsidian_black": "\033[38;2;58;58;58m", "ruby_red": "\033[38;2;155;17;30m", "sapphire_blue": "\033[38;2;15;82;186m", "topaz_yellow": "\033[38;2;255;200;124m"
}
reset_color = "\033[0m"

def papyrus_logo():

    shades_of_yellow_ansi = {
        "bright_yellow" : "\033[38;5;226m {}\033[00m",
        "orange_yellow" : "\033[38;5;220m {}\033[00m",
        "banana_yellow" : "\033[38;5;227m {}\033[00m",
        "pale_yellow" : "\033[38;5;228m {}\033[00m",
        "very_light_yellow" : "\033[38;5;229m {}\033[00m",
        "goldenrod" : "\033[38;5;178m {}\033[00m",
        "saffron" : "\033[38;5;214m {}\033[00m",
        "mustard" : "\033[38;5;136m {}\033[00m",
        "lemon_chiffon" : "\033[38;5;230m {}\033[00m",
        "chartreuse" : "\033[38;5;190m {}\033[00m",
    }
    shades_of_yellow_ansi_random = random.choice(list(shades_of_yellow_ansi.values()))
    
    def prYellow(s): print((shades_of_yellow_ansi_random).format(s))
    prYellow("""
....      ..                                                                           .x+=:.
+^""000h. ~"888h                               ..                                       z`    ^%
0X.  ?0000X  8888f               .d``          @L             .u    .      x.    .          .   <k
'008x  8888X  8888~        u      @8Ne.   .u   9888i   .dL   .d88B :@8c   .@88k  z88u      .@8Ned8"
'88888 8888X   "88x:    us888u.   %8888:u@88N  `Y888k:*888. ="8888f8888r ~"8888 ^8888    .@^%8888"
 `8888 8888X  X88x.  .@88 "8888"   `888I  888.   888E  888I   4888>'88"    8888  888R   x88:  `)8b.
   `*` 8888X '88888X 9888  9888     888I  888I   888E  888I   4888> '      8888  888R   8888N=*8888
  ~`...8888X  "88888 9888  9888     888I  888I   888E  888I   4888>        8888  888R    %8"    R88
   x8888888X.   `%8" 9888  9888   uW888L  888'   888E  888I  .d888L .+     8888 ,888B .   @8Wou 9%
  '%"*8888888h.   "  9888  9888  '*88888Nu88P   x888N><888'  ^"8888*"     "8888Y 8888"  .888888P`
  ~    888888888!`   "888*""888" ~ '88888F`      "88"  888      "Y"        `Y"   'YP    `   ^"F
       X888^""      ^Y"   ^Y'     888 ^              88F
       `88f                         *8E               98"
        88                          '8>             ./"
        ""                           "             ~`
""")


def create_folder():
    global colors, reset_color
    folder_name = 'Papyrus_Files'


    #FOLDER TO STORE FILES
    if not os.path.exists(folder_name):
        print(f'🔃{colors['neon_oasis']}Creating folder... {reset_color}', end='\r')

        os.mkdir(folder_name)
    else:
        print(f'✅{colors['jade_green']}Folder exists. {reset_color}', end='\r')   
        pass
    time.sleep(1)
    scribere()

def scribere():
    site_link = "https://oceanofpdf.com/?s="
    #SEARCH FOR BOOK TITLES
    search_query = input("\033[38;2;255;127;80m➤ Search Book Name: \033[0m").replace(' ','+')
    search_url = site_link + search_query.replace(' ', "+")

    #SCRAPE INFO
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")  
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
    service = Service(log_path="NUL") 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(search_url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    book_elements = soup.select("article[aria-label]")
    book_infos = soup.select("div.postmetainfo")
    book_w_link = []
    for article in book_elements:
        dl_element = article.select_one('a.entry-image-link')
        dl_link = dl_element.get('href') if dl_element else None

        book_w_link.append(dl_link)
    driver.quit()

    #SHOWING BOOK TITLES
    print(f'''\n{colors['phoenix_orange']}══════════════════════════════════════════════════════════════════════════════════
Literature Scan Results...
══════════════════════════════════════════════════════════════════════════════════{reset_color}''')
    for num, (book_title, info, dl_link) in enumerate(zip(book_elements, book_infos, book_w_link),start=1):
        title = (
            book_title['aria-label']
            .replace('Download', '')
            .replace('[PDF]', '')
            .replace('[EPUB]', '')
            .strip()
        )
        book_metadata = info.get_text(strip=True,  separator=" ")
        

        print(f"\n  {colors['pine_green']}└─ [{colors['rose_gold']}{num}{colors['pine_green']}] {colors['plasma_pink']}{title}{colors['pine_green']}\n    {colors['topaz_yellow']}{book_metadata}{reset_color}")

    print(f"""\n\n{colors['mint_fresh']}   [✓] Scan complete: Biblia extracted {reset_color}
   {colors['plasma_pink']}[✓] All files can be downloaded{reset_color}""")
    user_book_num_input = input(f"\n{colors['neon_starlight']}➤   Enter Book # (e = exit):{reset_color} ")
    match user_book_num_input:
        case 'e':
              os.system('cls' if os.name=='nt' else 'clear')
              exit
        case '1':
              webbrowser.open_new(book_w_link[0])
        case '2':
              webbrowser.open_new(book_w_link[1])
        case '3':
              webbrowser.open_new(book_w_link[2])
        case '4':
              webbrowser.open_new(book_w_link[3])
        case '5':
              webbrowser.open_new(book_w_link[4])
        case '6':
              webbrowser.open_new(book_w_link[5])
        case '7':
              webbrowser.open_new(book_w_link[6])
        
        




def main():
    os.system('cls' if os.name=='nt' else 'clear')
    papyrus_logo()
    print('\n')
    create_folder()
