
inventory = {}

def additem():
    item_name = input("Masukan nama barang: ")
    if item_name in inventory:
        print("Barang sudah ada di inventaris")
        return
    quantity = int(input("Masukan jumlah barang: "))
    price = int(input("Masukan harga barang: "))
    inventory[item_name]={"quantity":quantity, "price":price}
    print(f"{item_name} sudah dimasukan ke inventaris")

def update_qty():
    pass

def show_item():
    pass

def search_item():
    pass

def remove_item():
    pass

