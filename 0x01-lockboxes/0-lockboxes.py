#!/usr/bin/python3
# Adjacency matrices
from collections import deque

def canUnlockAll(boxes):
    opened = [0]
    keys = boxes[0]

    for k in keys:
        if k not in opened:
            opened.append(k)
            try:
                keys.extend([newkey for newkey in boxes[k] if newkey not in opened])
            except:
                pass
    if (len(opened) == len(boxes)):
        return True
    return False