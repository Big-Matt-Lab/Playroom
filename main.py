# Placeholder file to get started
# Let's change this to a real file when we have something to put here.
# score = 0
# for i in range(101):
#     score += 1
stuff = {'rope': 1, 'torch': 6, 'gold coins': 42, 'dagger': 1, 'arrow': 12}
new_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0
    for key, value in inventory.items():
        print(f"{value} {key}")
        item_total += value
    print(f"Total number of items: {item_total}")

display_inventory(stuff)