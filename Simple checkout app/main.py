import csv


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


def display_inventory():
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
        print(f"{item:<20}{details['quantity']:<15}{details['price']:<15}{item_value:<15}")
    print("-" * 50)
    print(f"Jumlah nilai inventaris: {total_value:.2f}\n")


def search_item():
    item_name = input("Masukan nama item: ").strip()
    if item_name not in inventory:
        print("item not found!")
        return
    details = inventory[item_name]
    print(f"Nama Barang: {item_name}")
    print(f"Jumlah: {details['quantity']}")
    print(f"Harga: {details['price']}")



def remove_item():
    item_name = input("Masukan nama item: ").strip()
    if item_name not in inventory:
        print("Barang tidak ditemukan")
        return
    del inventory[item_name]
    print(f"{item_name} sudah di hapus")

def save_inventory():
    with open("inventory.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(["Barang","Jumlah","Harga"])
        for item, details, in inventory.items():
            writer.writerow([item, details["quantity"], details["price"]])
    print("file inventaris ('inventory.csv') telah dibuat!")

def load_inventory():
    try:
        with open("inventory.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory[row["item"]]={
                    "quantity" : int(row["Quantitiy"]),
                    "price" : int(row["price"])
                }
        print("inventaris berhasil di muat")
    except FileNotFoundError:
        print("File inventaris tidak ditemukan. dimulau dengan inventaris kosong")

def main():
    load_inventory()
    while True:
        print("\n1. Tambah Barang")
        print("2. Perbarui Jumlah Barang")
        print("3. Tampilkan Inventaris")
        print("4. Cari Barang")
        print("5. Hapus Barang")
        print("6. Simpan dan Keluar")
        choice = input("Pilih opsi").strip()
        if choice == "1":
            additem()
        elif choice == "2":
            update_qty()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            search_item()
        elif choice == "5":
            remove_item()
        elif choice == "6":
            save_inventory()
            break
        else:
            print("Input salah, Masukan nomor yang benar (1-6)!")

if __name__ =="__main__":
    main()