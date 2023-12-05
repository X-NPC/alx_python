def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        length = 0
        first = "None"
        return length, first
    else:
        splitted = [ x for x in sentence ]
        first = splitted [0]
        return length, first
    
# zim ble sera sewye!
sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
