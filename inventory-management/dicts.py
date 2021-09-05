def create_inventory(items):
    '''

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    '''
    return {item:items.count(item) for item in items}

def add_items(inventory, items):
    '''

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    '''
    for item in items:
        if not inventory.get(item):
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1

    return inventory

def delete_items(inventory, items):
    '''

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    '''
    for item in items:
        if inventory.get(item) == 0:
            pass
        else:
            inventory[item] -= 1
    
    return inventory
    
def list_inventory(inventory):
    '''

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    '''
    return [(key, value) for key, value in inventory.items() if inventory.get(key) > 0]