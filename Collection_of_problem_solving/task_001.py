from random import sample

def list_rand_words(count: int, alp: str = 'абв'):
    word_list = []
    for i in range(count):
        letters = sample(alp, 3)
        word_list.append("".join(letters))
    return ' '.join(word_list)


def simple_sentence(words: str):
    return words.replace(' абв', '')


all_list = list_rand_words(int(input('Number of words: ')))
print(all_list)
print(simple_sentence(all_list))
