def eat_ghost(power_pellet_active, touching_ghost):
    '''

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    '''
    return True if power_pellet_active is True and touching_ghost is True else False

def score(touching_power_pellet, touching_dot):
    '''

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    '''
    return True if touching_power_pellet is True or touching_dot is True else False

def lose(power_pellet_active, touching_ghost):
    '''

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    '''
    return True if power_pellet_active is False and touching_ghost is True else False

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    '''

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    '''
    return True if has_eaten_all_dots is True and not lose(power_pellet_active, touching_ghost) else False