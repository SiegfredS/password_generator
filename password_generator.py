import random
import string
import numpy as np


class PasswordGenerator:

    def __init__(self,
                 num_digits:int,
                 num_letters:int,
                 num_special:int):
        self.num_letters = num_letters
        self.num_digits = num_digits
        self.num_special = num_special

    def generate_pass(self):
        letters = random.choices(population=string.ascii_letters, k=self.num_letters)
        digits = random.choices(population=string.digits, k=self.num_digits)
        special = random.choices(population=string.punctuation, k=self.num_special)
        to_shuffle = letters + digits + special
        np.random.shuffle(to_shuffle)
        return "".join(to_shuffle)

