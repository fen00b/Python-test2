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
    save_inventory()


def display_inventory():
    if not inventory:
        print("Inventaris kosong!")
        return
    print("\n Daftar Inventaris :")
    print(f"{'Barang':<20}{'Jumlah barang':<15}{'harga':<15}{'Nilai total':<15}")
    print("="*65)

    total_value = 0

    for item, details in inventory.items():
        status = "" #inizialize loop
        item_value = details["quantity"] * details["price"]
        total_value += item_value
        if details['quantity'] <=5:
            status = f"Stok {item} tersisa {details['quantity']}"
        print(f"{item:<20}{details['quantity']:<15}{details['price']:<15}{item_value:<15}{status:<10}")

    print("-" * 65)
    print(f"Jumlah nilai inventaris: Rp. {total_value:.2f}\n")

def stock_alert():
    for item in inventory:
        pass


def search_item():
    item_name = input("Masukan nama Barang: ").strip()
    if item_name not in inventory:
        print("Barang Tidak Ditemukan!")
        return
    details = inventory[item_name]
    print(f"Nama Barang: {item_name}")
    print(f"Jumlah: {details['quantity']}")
    print(f"Harga: {details['price']}")

def apply_disc():
    item_name = input("Masukan Nama barang: ").strip()
    if item_name not in inventory:
        print(f"{item_name} Tidak Ditemukan!")
        return
    discount = int(input("Masukan diskon"))
    if not (0 <= discount <=100):
        print("input yang dimasukan salah, masuka diskon antara 0-100%")
        return
    price_ori = inventory[item_name]['price']
    price_disc = price_ori*(1-discount/100)
    print(f"Harga {item_name} setelah diskon adalah {price_disc}")

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
                inventory[row["Barang"]]={
                    "quantity" : int(row["Jumlah"]),
                    "price" : int(row["Harga"])
                }
        print("inventaris berhasil di muat")
    except FileNotFoundError:
        print("File inventaris tidak ditemukan. dimulai dengan inventaris kosong")

def main():
    load_inventory()
    while True:
        print("\n1. Tambah Barang")
        print("2. Perbarui Jumlah Barang")
        print("3. Tampilkan Inventaris")
        print("4. Cari Barang")
        print("5. Cek Diskon")
        print("6. Hapus Barang")
        print("7. Simpan dan Keluar")
        choice = input("Pilih opsi: ").strip()
        if choice == "1":
            additem()
        elif choice == "2":
            update_qty()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            search_item()
        elif choice == "5":
            apply_disc()
        elif choice == "6":
            remove_item()
        elif choice == "7":
            save_inventory()
            break
        else:
            print("Input salah, Masukan nomor yang benar (1-6)!")

if __name__ =="__main__":
    main()