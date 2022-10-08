def rotate(text, key):
    fro = "abcdefghijklmnopqrstuvwxyz"
    to = fro[key:] + fro[:key]
    fro += fro.upper()
    to += to.upper()
    return text.translate(str.maketrans(fro, to))
