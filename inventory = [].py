inventory = []

def login():
    for _ in range(3):
        user = input("Username: ")
        password = input("Password: ")

        if user == "admin" and password == "1234":
            print("Login successful!")
            return True

        print("Incorrect login!")
    return False


def add_item():
    item_id = input("Item ID: ").strip()

    if not item_id or any(i[0] == item_id for i in inventory):
        print("Invalid or duplicate ID!")
        return

    name = input("Item Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    try:
        qty = int(input("Quantity: "))
        if qty < 0:
            print("Invalid quantity!")
            return
        minimum = int(input("Minimum: "))
        if minimum < 0:
            print("Invalid minimum!")
            return
    except ValueError:
        print("Enter a whole number!")
        return
      

    inventory.append([item_id, name, qty, minimum])
    print("Item added!")


def update_stock():
    item_id = input("Item ID: ").strip()

    for item in inventory:
        if item[0] == item_id:
            print("\n1. Stock In\n2. Stock Out")
            action = input("Choose: ").lower()

            try:
                qty = int(input("Quantity: "))
                if qty <= 0:
                    print("Quantity must be positive!")
                    return
            except ValueError:
                print("Invalid quantity!")
                return

            if action == "1":
                item[2] += qty
                print(qty, "stocks were added.")
              
            elif action == "2" and qty <= item[2]:
                item[2] -= qty
                print(qty, "stocks were used.")
              
            else:
                print("Invalid action or insufficient stock!")
                return

            print("Updated stock:", item[2])
            return

    print("Item not found!")


def view_inventory():
    if not inventory:
        print("Inventory is empty!")
        return

    for item in inventory:
      print("\n                  INVENTORY")  
      print(f"ID: {item[0]} | Name: {item[1]} | Quantity: {item[2]} | Minimum: {item[3]}" )

def low_stock():
  print("\n LOW STOCK ALERTS")

  found = False
  
  for item in inventory:
      if item[2] <= item[3]:
         print(
           "| Item:", item[1],
           "| Stock:", item[2],
           "| Minimum:", item[3]
         )
         found = True
        
  if found == False:
      print("No low-stock items.")

if login():
    while True:
        print("\n1. Add Item\n2. Update Stock\n3. View Inventory\n4. Low Stock Alert\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            low_stock()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")