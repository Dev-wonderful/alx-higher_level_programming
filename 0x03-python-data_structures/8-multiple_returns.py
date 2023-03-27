#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":
        return 0, None
    # elif sentence == "":
    #     return 0, None
    else:
        good = (len(sentence), sentence[0])
        return good
