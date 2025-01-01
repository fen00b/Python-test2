
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
    item_name = input("Masukan nama barang :").strip()
    if item_name not in inventory:
        print("barang tidak ada di inventaris")
        return
    quantity = int(input("Masukan jumlah barang :"))
    inventory[item_name]["quantity"]=quantity
    print(f"Jumlah {item_name} diubah menjadi {quantity}")


def inventory():
    if not inventory:
        print("Inventaris kosong!")
        return
    print("\n Daftar Inventaris :")
    print(f"{'Barang':<20}{'Jumlah barang':<15}{'harga':<15}{'Nilai total':<15}")
    print("="*65)

    total_value = 0

    for item, details in inventory.items():
        item_value = details["quantity"] * details["price"]
        total_value += item_value
        print(f"{item:<20}{details['quantity']:<10}{details['price']:<10}{item_value:<10}")
    print("-" * 50)
    print(f"Total Inventory Value: {total_value:.2f}\n")


def search_item():
    pass

def remove_item():
    pass

inventory()
