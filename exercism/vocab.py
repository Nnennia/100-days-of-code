import string


def add_prefix_un(word):
    """Add prefix
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Makes groups of words"""
    data = f'{vocab_words[0]} :: '
    data += ' :: ' .join([vocab_words[0] + word for word in vocab_words[1:]])
    return data


def remove_suffix_ness(word):
    """Remove suffix"""
    return word[:-5] + 'y' if word.endswith("iness") else word[:-4]


def adjective_to_verb(sentence, index):
    """Adjective to verb"""
    y = sentence.translate(str.maketrans('', '', string.punctuation))
    x = y.split()
    n = x[index]
    return n + "en"
  
