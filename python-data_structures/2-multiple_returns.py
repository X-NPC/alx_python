def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        length = 0
        first = None
        return lenght, first
    else:
        splitted = [ x for x in sentence ]
        first = splitted [0]
        return length, first
    
sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

