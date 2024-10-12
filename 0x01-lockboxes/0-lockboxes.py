#!/usr/bin/python3
""" Module contain canUnlockAll method
"""
from collections import deque


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened
    """
    opened = [0]
    keys = boxes[0]

    for k in keys:
        if k not in opened:
            opened.append(k)
            try:
                keys.extend([newkey for newkey in boxes[k]
                             if newkey not in opened])
            except Exception:
                pass
    if (len(opened) == len(boxes)):
        return True
    return False
