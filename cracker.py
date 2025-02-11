import time
import itertools
from tqdm import tqdm
from colorama import Fore
from hash_algorithm import HashAlgorithm
import os

class Cracker:
    def __init__(self, hash_type):
        self.hash_type = hash_type
        self.hash_algorithm = HashAlgorithm()

    def crack(self, target_hash, charset, min_length, max_length, language):
        print(Fore.MAGENTA + "\nCracking starts...\n" if language == 'english' else "\nÇözümleme başlıyor...\n")

        start_time = time.time()

        found = False
        result = None
        for length in range(min_length, max_length + 1):
            for guess in tqdm(itertools.product(charset, repeat=length), desc=f"Cracking... (Length: {length})" if language == 'english' else f"Çözülüyor... (Uzunluk: {length})",
                              total=len(charset) ** length,
                              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}, {rate_fmt}]"):
                guess_str = ''.join(guess)
                candidate_hash = self.hash_algorithm.hash_cracker(guess_str, self.hash_type)
                if candidate_hash == target_hash:
                    result = guess_str
                    found = True
                    break
            if found:
                break

        end_time = time.time()
        duration = end_time - start_time

        if found:
            print(Fore.GREEN + f"Hash solution found: {result}" if language == 'english' else f"Hash çözümü bulundu: {result}")
            input(Fore.CYAN + "Press enter to continue..." if language == 'english' else "Devam etmek için enter tuşuna basın...")
            os.system('cls')
        else:
            print(Fore.RED + ("Solution not found." if language == 'english' else "Çözüm bulunamadı."))
        
        print(Fore.CYAN + f"Time: {duration:.2f} seconds." if language == 'english' else f"Zaman: {duration:.2f} saniye.")
