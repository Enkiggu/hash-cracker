import os
import time
from colorama import Fore, init
from menu import Menu
from hash_algorithm import HashAlgorithm
from user_input import UserInput
from cracker import Cracker

init(autoreset=True)

def main():
    os.system('cls')
    menu = Menu()
    menu.display_language_selection()
    
    language_choice = input(Fore.MAGENTA + "Please enter your choice / Lütfen seçenek giriniz: ").strip()
    language = menu.get_language(language_choice)
    
    while True:
        os.system('cls')
        menu.display_main_menu(language)
        
        choice = input(Fore.MAGENTA + ("Enter your choice: " if language == 'english' else "Bir seçenek girin: ")).strip()
        
        if choice == '0':
            print(Fore.RED + ("Exiting..." if language == 'english' else "Çıkılıyor..."))
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print(Fore.YELLOW + ("Invalid option, please try again." if language == 'english' else "Geçersiz seçenek, lütfen tekrar deneyin."))
            continue
        
        hash_algorithm = HashAlgorithm()
        hash_type = hash_algorithm.get_hash_type(choice)
        
        user_input = UserInput(language)
        target_hash, charset, min_length, max_length = user_input.get_inputs()
        
        cracker = Cracker(hash_type)
        cracker.crack(target_hash, charset, min_length, max_length, language)
        
if __name__ == "__main__":
    main()
