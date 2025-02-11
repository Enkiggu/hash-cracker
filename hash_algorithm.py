import hashlib

class HashAlgorithm:
    def get_hash_type(self, choice):
        hash_types = {
            '1': 'sha256',
            '2': 'md5',
            '3': 'sha1',
            '4': 'sha512',
            '5': 'sha224',
            '6': 'sha384',
            '7': 'sha3_256'
        }
        return hash_types.get(choice, None)

    def hash_cracker(self, candidate_str, hash_type):
        if hash_type == 'sha256':
            return hashlib.sha256(candidate_str.encode()).hexdigest()
        elif hash_type == 'md5':
            return hashlib.md5(candidate_str.encode()).hexdigest()
        elif hash_type == 'sha1':
            return hashlib.sha1(candidate_str.encode()).hexdigest()
        elif hash_type == 'sha512':
            return hashlib.sha512(candidate_str.encode()).hexdigest()
        elif hash_type == 'sha224':
            return hashlib.sha224(candidate_str.encode()).hexdigest()
        elif hash_type == 'sha384':
            return hashlib.sha384(candidate_str.encode()).hexdigest()
        elif hash_type == 'sha3_256':
            return hashlib.sha3_256(candidate_str.encode()).hexdigest()
        return None
