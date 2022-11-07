
def answer(question):
    question = question.replace("What is", "").replace("?","")\
        .replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/").strip()

    question = list(reversed(question.split(" ")))
    print(question)
    if question == [""]:
        raise ValueError("syntax error")
    while len(question) != 1:
        if len(question) < 3:
            left = question.pop()
            if not left:
                raise ValueError("syntax error")
            operation = question.pop()
            if operation not in "-/*+":
                try:
                    int(operation)
                except:
                    raise ValueError("unknown operation")
                else:
                    raise ValueError("syntax error")
            raise ValueError("syntax error")
        else:
            left = question.pop()
            operation = question.pop()
            right = question.pop()

        if left in "-/*+" or  right in "-/*+":
            raise ValueError("syntax error")
        if operation not in "-/*+" :
            raise ValueError("unknown operation")
        question.append(str(eval(left+operation+right)))
    return int(float(question[0]))
