import pyfiglet
from colorama import Fore

class Menu:
    def __init__(self):
        self.ascii_art = '''
        \t      _________
        \t     / ======= \\
        \t    / __________\\
        \t   | ___________ |
        \t   | | -       | |
        \t   | |         | |
        \t   | |_________| |_________________________
        \t   \=____________/   github.com/enkiggu    )
        \t   / """"""""""" \                        /
        \t  / ::::::::::::: \                   =D-'
        \t (_________________)
        '''

    def display_language_selection(self):
        print(Fore.YELLOW + "Select language / Dil seçin:")
        print(Fore.CYAN + "[1] English")
        print(Fore.CYAN + "[2] Türkçe")
        
    def get_language(self, language_choice):
        if language_choice == '1':
            return 'english'
        elif language_choice == '2':
            return 'turkish'
        else:
            print(Fore.RED + "Invalid selection! Defaulting to English.")
            return 'english'

    def display_main_menu(self, language):
        print(Fore.GREEN + self.ascii_art)
        ascii_banner = pyfiglet.figlet_format(" Hash Cracker" if language == 'english' else "  Hash     Kırıcı")
        print(Fore.GREEN + ascii_banner)
        
        menu = '''
        [1] SHA-256 Hash Cracker
        [2] MD5 Hash Cracker
        [3] SHA-1 Hash Cracker
        [4] SHA-512 Hash Cracker
        [5] SHA-224 Hash Cracker
        [6] SHA-384 Hash Cracker
        [7] SHA-3-256 Hash Cracker
        [0] Exit
        ===============================
        ''' if language == 'english' else '''
        [1] SHA-256 Hash Kırıcı
        [2] MD5 Hash Kırıcı
        [3] SHA-1 Hash Kırıcı
        [4] SHA-512 Hash Kırıcı
        [5] SHA-224 Hash Kırıcı
        [6] SHA-384 Hash Kırıcı
        [7] SHA-3-256 Hash Kırıcı
        [0] Çıkış
        ===============================
        '''
        print(Fore.CYAN + menu)
