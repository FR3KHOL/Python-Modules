import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item_name>:<quantity>")
        return

    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts = arg.split(':')

        if len(parts) != 2:
            print(f"Error invalid parameter '{arg}'")
            continue
        item = parts[0]
        qty_str = parts[1]
        if item in inventory:
            print(f"Redundant item '{item}' discarding")
            continue
        try:
            qty = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    if len(inventory) == 0:
        return

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    total_items = len(inventory)
    print(f"Total quantity of the {total_items} items: {total_qty}")

    for item in inventory.keys():
        qty = inventory[item]
        percentage = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_item = ""
    most_qty = -1
    least_item = ""
    least_qty = float('inf')

    for item in inventory.keys():
        qty = inventory[item]
        if qty > most_qty:
            most_qty = qty
            most_item = item
        if qty < least_qty:
            least_qty = qty
            least_item = item

    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
