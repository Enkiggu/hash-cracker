import string

class UserInput:
    def __init__(self, language):
        self.language = language

    def get_inputs(self):
        target_hash = input("Enter the hash value to be cracked: ").strip()

        use_lower = input("Use lowercase letters? (y/n): ").strip().lower() or 'n'
        use_upper = input("Use uppercase letters? (y/n): ").strip().lower() or 'n'
        use_digits = input("Use numbers? (y/n): ").strip().lower() or 'n'
        use_special = input("Use symbols? (y/n): ").strip().lower() or 'n'

        charset = ''
        if use_lower == 'y':
            charset += string.ascii_lowercase
        if use_upper == 'y':
            charset += string.ascii_uppercase
        if use_digits == 'y':
            charset += string.digits
        if use_special == 'y':
            charset += string.punctuation

        min_length = input("Enter the minimum length (default 1): ").strip()
        min_length = int(min_length) if min_length else 1

        max_length = input("Enter the maximum length (default 25): ").strip()
        max_length = int(max_length) if max_length else 25
        
        return target_hash, charset, min_length, max_length
