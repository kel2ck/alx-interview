#!/usr/bin/python3
"""
Solves the lock boxes challenge
"""


def canUnlockAll(boxes):
    unlocked = set([0])

    for box_id, box in enumerate(boxes):
        if not box_id in unlocked:
            continue
        for key in box:
            if key < len(boxes):
                unlocked.add(key)

    return len(unlocked) == len(boxes)
