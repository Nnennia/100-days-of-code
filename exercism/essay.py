def capitalize_title(title):
    """Capitalizes the first letter of each word

    Args:
        title (str)
    """
    return title.title()


def check_sentence_ending(sentence):
    """Check punctuation
    """
    return sentence.endswith(".")

def clean_up_spacing(sentence):
    """Removes unnecessary spacing
    """
    new_sentence = " ".join(sentence.split())
    return new_sentence


def replace_word_choice(sentence, old_word, new_word):
    """Replaces words in a string"""
    new_sentence = sentence.replace(old_word, new_word)
    return new_sentence
