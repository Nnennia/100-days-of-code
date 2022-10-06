def create_inventory(items):
    inventory = {}
    for key in items:
        inventory[key] = inventory.setdefault(key, 0) + 1
    return inventory


def add_items(item, inventory):
    for key in item:
        inventory[key] = inventory.setdefault(key, 0) + 1
    return inventory


def decrement_items(inventory, items):
    inventory = {}
    for key in items:
        if inventory[key]:
            inventory[key] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    return [(key, value) for (key, value) in inventory.items()
            if value > 0]
