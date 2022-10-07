def is_paired(input_string):
    brackets = "".join(char for char in input_string if char in "{}[]()")
    while (pair := next((pair for pair in ("{}", "[]", "()") if pair in brackets), False)):
        brackets = brackets.replace(pair, "")
    return not brackets
