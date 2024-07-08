#!/usr/bin/python3

"""
    Create a func where prototype -> canUnlockAll(boxes)
    to loop through a list and return boolean state of Boxes
    unlockability 🤭
"""


def canUnlockAll(boxes) -> bool:
    """
        Check if boxes can be unlocked
    """

    if len(boxes) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx, box in enumerate(boxes):
            boxes_checked = k in box and k != idx
            if boxes_checked:
                break

        if boxes_checked is False:
            return boxes_checked
    return True
