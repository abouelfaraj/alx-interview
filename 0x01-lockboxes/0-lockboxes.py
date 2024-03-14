def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened."""
    if not isinstance(boxes, list):
        return False
    if not all(isinstance(bx, list) for bx in boxes):
        return False

    keys = [0]
    visited = set(keys)

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in visited and 0 <= key < len(boxes):
                keys.append(key)
                visited.add(key)

    return len(visited) == len(boxes)
