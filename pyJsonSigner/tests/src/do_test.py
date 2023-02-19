from pyjsonsigner import sig
import json
import nltk
import random
import unittest

def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownModule')


class TestSign(unittest.TestCase):
    def setUp(self):
        nltk.download('words')
        self.word_set = self.generate_word_set(size=100)

    def tearDown(self):
        pass

    def test_simple_sign(self):
        j = json.loads('{"key":"value"}')
        token = sig.sign(j)
        self.assertEqual(token, '88bac95f31528d13a072c05f2a1cf371')

    def test_complex_sign(self):
        random_obj = self.generate_random_json_object(num_keys=5, depth=3)
        print(json.dumps(random_obj, indent=4))

        token = sig.sign(random_obj)
        verifysign = sig.verifysign(random_obj, token)
        self.assertTrue(verifysign)


    def generate_word_set(self,size=100):
        words = set(nltk.corpus.words.words())
        word_list = list(words)
        random.shuffle(word_list)
        return set(word_list[:size])

    def generate_random_json_object(self, num_keys, depth=1):
        # load the list of English words
        with open('/usr/share/dict/words') as f:
            words = f.read().splitlines()

        # create an empty dictionary for the object
        obj = {}

        # populate the dictionary with random key-value pairs
        for i in range(num_keys):
            # generate a random word for the key
            key = random.choice(words)

            # generate a random value (either a string, a number, or another nested object)
            if depth > 1 and random.choice([True, False]):
                value = self.generate_random_json_object(num_keys, depth=depth - 1)
            elif random.choice([True, False]):
                value = ''.join(
                    random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
            else:
                value = random.uniform(0, 100)

            # add the key-value pair to the dictionary
            obj[key] = value

        # return the object
        return obj
