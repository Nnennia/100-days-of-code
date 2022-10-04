def pig_latin(word):
    word = word.strip().lower()
    pig_latin =''
    vowel = ['a','e','i','o','u']
    for i in range(len(word)):
        if word[i] in vowel:
            if i==0:
                word+="w"
            pig_latin+=word[i:]+word[0:i]+"ay"
            break
    return pig_latin
  
