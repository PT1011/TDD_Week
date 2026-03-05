def add_item(inventory, item):
    if item == "":
        raise ValueError("Please add a valid item to inventory")
    elif len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError("Inventory is at max capacity")
    elif inventory["locked"] == True:
        return inventory
    else:
        inventory["items"].append(item)
        return inventory

def remove_item(inventory, item):
    pass

def get_item_count(inventoru):

    pass
