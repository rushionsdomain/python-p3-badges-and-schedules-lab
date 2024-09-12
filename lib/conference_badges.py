def badge_maker(name):
    """Creates and returns a badge with the given name."""
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    """Creates and returns a list of badges for each name in the provided list."""
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    """Creates and returns a list of welcome messages and room assignments."""
    return [f"Hello, {name}! You'll be assigned to room {i + 1}!" for i, name in enumerate(names)]

def printer(names):
    """Prints out the badges and room assignments."""
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    output = "\n".join(badges + rooms)
    print(output)