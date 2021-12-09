#P99.5.6.2
#inventory.py
stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(v,end='')
        print('    ',end='')
        print(k)
        item_total=item_total+v
    print('Total number of items:  '+str(item_total))
displayInventory(stuff)


#99.5.6.3
def addToInventory(inventory,addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]=inventory[i]+1
        else:
            inventory[i]=1
    return inv
inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','ruby']
inv=addToInventory(inv,dragonLoot)
#problems
displayInventory(inv)
        
