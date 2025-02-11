# Hash Cracker Tool

A Python-based basic hash cracking tool that supports multiple hash algorithms. This tool allows you to crack various types of hashes including SHA-256, MD5, SHA-1, SHA-512, SHA-224, SHA-384, and SHA-3-256. You can customize the character set used for the cracking process and specify minimum and maximum lengths for the guessed strings.

## Features

- **Supports multiple hash algorithms:**
  - SHA-256
  - MD5
  - SHA-1
  - SHA-512
  - SHA-224
  - SHA-384
  - SHA-3-256
- **Customizable charset:** Choose which characters to include (lowercase, uppercase, numbers, and special symbols).
- **Brute-force cracking:** Cracks hashes by brute-forcing combinations of characters in the specified range.
- **Multilingual interface:** Available in both English and Turkish.

## Requirements

- Python 3.x
- Required Python libraries:
  - `tqdm` for progress bars
  - `colorama` for colorful output
  - `pyfiglet` for ASCII art

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
1. **Clone this repository**:
```bash
git clone https://github.com/yourusername/hash-cracker.git
cd hash-cracker
```
2. **Run the application**:
```bash
python hash_cracker.py
```
3. **Follow the on-screen prompts**:
  - Select your language (English or Turkish).
  - Choose a hash algorithm.
  - Enter the hash value you want to crack.
  - Select the character sets you want to use (lowercase, uppercase, digits, symbols).
  - Set the minimum and maximum length for the string combinations.
4. **The tool will attempt to find the original string that corresponds to the given hash**.

## Example

Here's an example of running the tool:

```bash
Select language / Dil seçin:
[1] English
[2] Türkçe
Please enter your choice / Lütfen seçenek giriniz: 1

Hash Cracker
[1] SHA-256 Hash Cracker
[2] MD5 Hash Cracker
[3] SHA-1 Hash Cracker
[4] SHA-512 Hash Cracker
[5] SHA-224 Hash Cracker
[6] SHA-384 Hash Cracker
[7] SHA-3-256 Hash Cracker
[0] Exit
===============================

Enter your choice: 1
Enter the hash value to be cracked: e99a18c428cb38d5f260853678922e03
Use lowercase letters? (y/n): y
Use uppercase letters? (y/n): n
Use numbers? (y/n): y
Use symbols? (y/n): n
Enter the minimum length (default 1): 1
Enter the maximum length (default 25): 5

Cracking starts...
...
Hash solution found: test1
Time: 0.12 seconds.
```

## Contributing
Feel free to fork this repository and submit pull requests. If you find bugs or have suggestions for improvements, open an issue in the GitHub repository.





