# Improve the password generator below,
# such as it is able to generate passwords that also contain numbers and special characters.
#
# Note: random.randrange(0, x) will generate a single random number from a to x
#
# Note: the string module may also have other useful characters information

import string
import random

all_letters = list(string.ascii_letters)
all_punctuation = list(string.punctuation)
all_digits = list(string.digits)
print(all_letters)
pass_length = int(input('Pass length : '))
chooser_roulette_old = ''
password = ''
for a in range(pass_length):
    chooser_roulette = random.randrange(1, 4)
    if chooser_roulette != chooser_roulette_old:
        if chooser_roulette == 1:
            sign_index = random.randrange(0, len(all_punctuation))
            password += all_punctuation[sign_index]
        elif chooser_roulette == 2:
            letter_index = random.randrange(0, len(all_letters))
            password += all_letters[letter_index]
        else:
            digit_index = random.randrange(0, len(all_digits))
            password += all_digits[digit_index]
    else:
        if chooser_roulette == 3:
            sign_index = random.randrange(0, len(all_punctuation))
            password += all_punctuation[sign_index]
        elif chooser_roulette == 1:
            letter_index = random.randrange(0, len(all_letters))
            password += all_letters[letter_index]
        else:
            digit_index = random.randrange(0, len(all_digits))
            password += all_digits[digit_index]
    chooser_roulette_old = chooser_roulette
print("Generated Password : ", password)
