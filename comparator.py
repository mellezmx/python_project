from functools import cmp_to_key


class Alphabet():

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def compare_words(self, word1, word2):

        # return 1 when the index in the new alphabet of word1 is greater that word2 (ex: az > za)
        # in other words word1 come after word2.

        for n in range(len(min([word1, word2], key=len))):
            if self.alphabet.index(word1[n]) != self.alphabet.index(word2[n]):
                if self.alphabet.index(word1[n]) > self.alphabet.index(word2[n]):
                    return 1
                else:
                    return -1
        if len(word1) > n + 1:
            return 1
        elif len(word2) > n + 1:
            return -1
        return 0


    def my_sort(self, text):
        text_to_list = text.split()
        cmp_items_py3 = cmp_to_key(self.compare_words)
        text_to_list.sort(key = cmp_items_py3)
        return text_to_list

new_alphabet = Alphabet(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p',
 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])


my_text = 'because this is the next tool i want to enable'

new_text = new_alphabet.my_sort(my_text)
print(new_text)
