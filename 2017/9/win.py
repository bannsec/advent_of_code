#!/usr/bin/env python

with open("input","r") as f:
    inp = f.read().strip()

def parse_group(group, score=1):
    """group = character string, excluding the first and end curly brackets.
    
    score is really the depth. it increments by one when you go down a level."""
    global garbage_chars
    group_score = score

    ignore_next = False
    garbage = False

    # Use i to keep track of position
    i = -1
    while i < len(group)-1:
        i += 1
        c = group[i]

        if ignore_next:
            ignore_next = False
            continue

        if c == "!":
            ignore_next = True
            continue

        # If we're not inside garbage tags
        if not garbage:

            if c == "{":
                # Find group
                sub_group = extract_group(group[i:])
                group_score += parse_group(sub_group, score=score+1)
                # Need to update our index to be past this group
                i += len(sub_group) + 1 # Subgroup does NOT contain it's own {} in the count
                assert group[i] == "}", "Somehow didn't hit the end of the group where expected."

            elif c == "<":
                garbage = True

        # If we're inside garbage tags, only worry about closing them
        else:

            if c == ">":
                garbage = False

            else:
                garbage_chars += 1


    return group_score


def extract_group(group):
    """Given a char stream group, assuming the group starts at char[0], identify where the group ends and return only those things inside the group."""
    assert group[0] == "{", "This is not the start of a group."

    curly_count = 0
    inside_group = ""
    ignore_next = False
    garbage = False # Inside garbage tags?

    for c in group:
        inside_group += c

        # The "!" ignore chars
        if ignore_next:
            ignore_next = False
            continue

        # Special ignore char works everywhere
        if c == "!":
            ignore_next = True
            continue

        # If we're not inside garbage tags
        if not garbage:

            if c == "{":
                curly_count += 1
            elif c == "}":
                curly_count -= 1
            elif c == "<":
                garbage = True

        # If we're inside garbage tags, only worry about closing them
        else:

            if c == ">":
                garbage = False

        # We found the end
        if curly_count == 0:
            return inside_group[1:-1] # Trim the "{}"

        # This char is inside the group, add it
    else:
        raise Exception("Couldn't find the end of inside the group!")

garbage_chars = 0

total_score = parse_group(extract_group(inp))
print(total_score)
print(garbage_chars)
