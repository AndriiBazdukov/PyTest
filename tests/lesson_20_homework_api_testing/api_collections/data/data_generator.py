import string
from random import Random


class DataGenerator:

    @staticmethod
    def get_string_of_length(length):
        random = Random()
        res = ''.join(random.choices(string.ascii_letters, k=length))
        return res
