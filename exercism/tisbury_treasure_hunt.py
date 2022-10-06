def get_coordinate(record: tuple):
    """Takes a pair treause and coordinate and returns coordinate"""
    return record[1]


def convert_coordinate(coordinate: str):
    """Return a tuple"""
    return tuple(coordinate)


def compare_records(treasure_coordinate, location_coordinate):
    """Returns a tuple is the two coordinates are equal"""
    return (treasure_coordinate[1] == location_coordinate[1])


def create_record(treasure_coordinate, location_coordinate):
    if not compare_records(treasure_coordinate, location_coordinate):
        return "not a match"
    return *treasure_coordinate, *location_coordinate


def clean_up(combined_record_group):
    """Returns tuples of tuples"""
    data = [(x[0], x[2], x[3], x[4]) for x in combined_record_group]
    lines = [f"{x}\n" for x in data]
    return "".join(lines)
