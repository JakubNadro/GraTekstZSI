from gra.game import Location

stack = [
    1
]


def szukanie(droga):
    # Fix circular inputs
    from gra.config import locations

    for i in range(0, len(locations)):
        if locations[i]['id'] == droga:
            return locations[i]


def get_curr_location() -> Location:
    return szukanie(stack.top())


def get_previous_location() -> Location:
    curr_location = stack.top()
    stack.pop()
    prev_location = szukanie(stack.top())
    stack.append(curr_location)
    return prev_location


def move(droga):
    print(get_curr_location().entry_msg)
