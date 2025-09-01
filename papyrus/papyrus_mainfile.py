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
import requests
import sys
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

def scribere():
    folder_name = 'Papyrus_Files'
    site_link = "https://oceanofpdf.com/?s="

    #FOLDER TO STORE FILES
    if not os.path.exists(folder_name):
        print('🔃 Creating folder... ', end='\r')

        os.mkdir(folder_name)
    else:
        print('✅ Folder exists.', end='\r')   
        pass
         
    time.sleep(1)

    #SEARCH FOR BOOK TITLES
    search_query = input("\033[38;2;255;127;80m➤ Search Book Name: \033[0m").replace(' ','+')
    if len(search_query.strip()) == 0:
        return main()
    search_url = site_link + search_query.replace(' ', "+")

    #SCRAPE INFO
    chrome_options = Options()

    service = Service(log_path="NUL") 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(search_url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    book_elements = soup.select("article[aria-label]")
    book_infos = soup.select("div.postmetainfo")

    driver.quit()

    #SHOWING BOOK TITLES
    print(f'''\n══════════════════════════════════════════════════════════════════════════════════
Literature Scan Results...
══════════════════════════════════════════════════════════════════════════════════''')
    for num, (book_title, info) in enumerate(zip(book_elements, book_infos),start=1):
        title = (
            book_title['aria-label']
            .replace('Download', '')
            .replace('[PDF]', '')
            .replace('[EPUB]', '')
            .strip()
        )
        book_metadata = info.get_text(strip=True,  separator=" ")
        

        print(f"\n  └─ [{num}] {title}\n    {book_metadata:5}")

    print("""\n\n   [✓] Scan complete: Biblia extracted
   [✓] All files can be downloaded""")
    user_book_num_input = input("\n➤   Enter Book #: ")








def main():
    os.system('cls' if os.name=='nt' else 'clear')
    papyrus_logo()
    print('\n')
    scribere()

 
