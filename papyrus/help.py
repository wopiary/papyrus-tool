import os, time

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

def help_info():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"{colors['sahara_beige']}Papyrus{reset_color} is a tool that helps you find literature, also known as digital {colors['sunset_orange']}\"scribes\"{reset_color} or {colors['golden_dune']}\"papyrus\"{reset_color}, scattered across the vast {colors['coyote_brown']}interwebs{reset_color}.")
    print(f"Think of it as your personal librarian, scouring the web for knowledge and bringing it back to you in one place.\n")
    
    print(f"{colors['clay_red']}1   Launch Papyrus.{reset_color}")
    print(f"{colors['coyote_brown']}2   Enter your query for literature or \"scribes.\"{reset_color}")
    print(f"{colors['sunset_orange']}3   Papyrus searches the interwebs for relevant digital scrolls.{reset_color}")
    print(f"{colors['golden_dune']}4   Browse, save, or export the collected works.{reset_color}\n")
    
    while True:
        user_input = input(f"{colors['coyote_brown']}[e]{colors['sunset_orange']} to{colors['coyote_brown']} Exit:{reset_color} ").strip().lower()
        if user_input == 'e':
            return 'back'
        else:
            print(f"{colors['clay_red']}Invalid input, staying in the current menu.{reset_color}")
            return help_info()

