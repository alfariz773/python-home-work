# Step 1: Start with empty inventory
inventory=[]
# Step 2: Add first item
def add_item():
    inventory.append("dog food")
    return inventory
print(add_item())
# Step 3: Add remaining items
def add_more():
    inventory.append("cat toy")
    inventory.append("fish tank")
    inventory.append("bird cage")
    return inventory
print(add_more())
# Step 4: Display each item nicely using lambda
item = lambda x : print("item in stock",x)
for x in inventory:
    
    item(x) 
# Step 5: Recursive function to count total items    
def total_stock(inventory,i=0):
    if i==len(inventory):
        return 0
    return 1 + total_stock(inventory, i + 1)
print("Total number of items:", total_stock(inventory))
