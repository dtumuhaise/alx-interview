#!/usr/bin/python3
""" method that determines if all the
boxes can be opened """


def canUnlockAll(boxes):
    """ method that determines if all the
    boxes can be opened """
    if boxes is None:
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
