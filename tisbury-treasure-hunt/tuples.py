def get_coordinate(record):
    '''

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    '''
    return record[1]
    
def convert_coordinate(coordinate):
    '''

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    '''
    return (coordinate[0], coordinate[1])
    
def compare_records(azara_record, rui_record):
    '''

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    '''
    return True if azara_record[1] == rui_record[1][0] + rui_record[1][1] else False
    
def create_record(azara_record, rui_record):
    '''

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    '''
    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'

def clean_up(combined_record_group):
    '''

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: tuple of tuples - everything "cleaned", with excess coordinates and information removed.
    '''
    s = ''

    for outer_tuple in combined_record_group:
        s += str((outer_tuple[0], outer_tuple[2], outer_tuple[3], outer_tuple[4])) + '\n'
    
    return s