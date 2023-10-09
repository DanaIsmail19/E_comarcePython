from Admin import Admin
from Product import Product
from Shopper import Shopper

products = []
Shoppers = []
Admins = []

class OnlineStore:
    def __init__(self):
       self.product = []
       self.user = []

    # Implement other methods for admin and shopper actions here
#this function for checking if the user is admin or not
def Admin_only_checking():
        # Ask the user to enter a user ID
    userID = input("Enter your admin user ID: ")

    # Check if the user ID exists in the list of admins
    admin_user = None
    for admin in Admins:      # Assuming Admin is a list of Admin objects
        if admin.user_id == userID:
            admin_user = admin
            break

    if admin_user is None:
        print("Access denied. User ID does not exist or you are not an admin.")
        return 1


def shopper_admin_checking():
    # Ask the user to enter a user ID
    userID = input("Enter your user ID: ")

    # Check if the user ID exists in the list of shoppers
    shopper_user = None
    for shopper in Shoppers:  # Assuming shopper is a list of Shopper objects
        if shopper.user_id == userID:
            shopper_user = shopper
            break
    admin_user = None
    for admin in Admins:  # Assuming Admin is a list of Admin objects
        if admin.user_id == userID:
            admin_user = admin
            break

    if shopper_user is None and admin_user is None:
        print("Access denied. User ID does not exist or you are not a shopper or admin.")
        return 1


def shopper_only_checking():
     # Ask the user to enter a user ID
        userID = input("Enter your user ID: ")

        # Check if the user ID exists in the list of shoppers
        shopper_user = None
        for shopper in Shoppers:  # Assuming shopper is a list of Shopper objects
            if shopper.user_id == userID:
                shopper_user = shopper
                break

        if shopper_user is None:
            print("Access denied. User ID does not exist or you are not a shopper.")
            return 1

    





def add_product(): #admin only
    # Implement Add product
    if Admin_only_checking() == 1 :
        return
    print("__________enter the following product information_________")
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    inventory = int(input("Enter product inventory: "))
    supplier = input("Enter product supplier: ")
    has_an_offer = input("Does the product have an offer? (yes/no): ")

    if has_an_offer == '1':
            offer_price = float(input("Enter offer price: "))
            valid_until = input("Enter offer valid until (YYYY-MM-DD): ")
    else:
            offer_price = None
            valid_until = None

    product = Product(
            product_id,
            name,
            category,
            price,
            inventory,
            supplier,
            has_an_offer,
            offer_price,
            valid_until
    )
    products.append(product)
    for product in products:
            product.display_product_info()


def place_item_on_sale():
    # Implement Place an item on sale
    if Admin_only_checking() == 1:
        return

    productID= input("Please enter the product id you want to make an offer on :")

    product_item = None

    for product in products: # Assuming shopper is a list of Shopper objects

        if product.product_id == productID:

            product_item = product
            break

    if product_item is None:
        print("____Product does not exist.____")
        return
    for product in products:
        if product.product_id == productID:
            if product.has_offer == '1':
                print("Sorry, this product already has an offer, its valid until: "+ product_item.valid_until)
            else:
                 print("________This product has no offer you can place an offer_______")
                 product.has_offer='1'
                 offer_price = float(input("Enter offer price: "))
                 valid_until = input("Enter offer valid until (YYYY-MM-DD): ")
                 product.offer_price=offer_price
                 product.valid_until=valid_until


    for product in products:
            product.display_product_info()




def update_product():
    # Implement Update product
    if Admin_only_checking() == 1:
        return
    productID = input("Please enter the product id you want to update :")

    product_item = None

    for product in products:

        if product.product_id == productID:
            product_item = product
            break

    if product_item is None:
        print("____Product does not exist.____")
        return
    choice= input("What whould you like to change : 1)product name 2)category 3)product price 4)product inventory 5)product supplier 6)product offer" )
    if choice =='1':
        newNAME=input("Enter the new product name :")
        for product in products:
            if product.product_id == productID:
                product.name=newNAME
    elif choice =='2':
        newCATEGORY = input("Enter the new product category :")
        for product in products:
            if product.product_id == productID:
                product.category=newCATEGORY
    elif choice == '3':
        newPRICE = input("Enter the new product price :")
        for product in products:
            if product.product_id == productID:
                product.price=newPRICE
    elif choice == '4':
        newINVETORY = input("Enter the new product inventory :")
        for product in products:
            if product.product_id == productID:
                product.inventory=newINVETORY
    elif choice == '5':
        newSUPPLIER = input("Enter the new product supplier :")
        for product in products:
            if product.product_id == productID:
                product.supplier=newSUPPLIER
    elif choice == '6':
        newoffer_price = float(input("Enter offer price: "))
        newvalid_until = input("Enter offer valid until (YYYY-MM-DD): ")
        for product in products:
            if product.product_id == productID:
                product.has_offer = '1'
                product.offer_price = newoffer_price
                product.valid_until = newvalid_until
    else :
        print("invalid choice. ")
        return
    for product in products:
            product.display_product_info()

def add_new_user():
    # Implement Add a new user
    if Admin_only_checking() == 1:
        return

    # Function to validate a 6-digit ID
    def validate_id(id):
        return id.isdigit() and len(id) == 6

    # Check if he wants to add an admin or shopper
    choice = input("Do you want to enter a new admin or shopper? ").lower()
    
    if choice == "admin":
        print("___________Please fill the admin information_________")
    elif choice == "shopper":
        print("___________Please fill the shopper information_________")
    else:
        print("_____________________")
        print("Please enter 'admin' or 'shopper' for the new user.")
        print("_____________________")
        return

    user_id = input("Enter user ID (6 digits): ")
    
    # Validate the user ID
    if not validate_id(user_id):
        print("Invalid user ID. Please enter a 6-digit ID.")
        return
    
    # Check if the ID already exists
    for user in Admins + Shoppers:
        if user.user_id == user_id:
            print("User with this ID already exists. Please choose another ID.")
            return

    name = input("Enter user name: ")
    date_of_birth = input("Enter user date of birth (YYYY-MM-DD): ")
    role = int(input("Enter user role (0 for admin, 1 for shopper): "))
    active = int(input("Enter user activity (0 for not active, 1 for active): "))
    
    if choice == "admin":
        admin = Admin(
            user_id,
            name,
            date_of_birth,
            role,
            active
        )
        Admins.append(admin)
    elif choice == "shopper":
        shopper = Shopper(
            user_id,
            name,
            date_of_birth,
            role,
            active,
            ready_to_order=0,
        )
        Shoppers.append(shopper)

    # Display information for admin users
    for admin in Admins:
        admin.display_user_info()

    # Display information for shopper users
    for shopper in Shoppers:
        shopper.display_user_info()




def update_user():
    # Implement Update user
    if Admin_only_checking() == 1:
        return

    # Ask the admin for the user code to update
    user_id = input("Enter the user ID to update (6 digits only): ")

    # Check if the user ID contains exactly 6 digits
    if not user_id.isdigit() or len(user_id) != 6:
        print("Invalid user ID format. Please enter a 6-digit user ID.")
        return

    # Check if the user exists in the list of users (both admins and shoppers)
    user = None
    for admin in Admins:
        if admin.user_id == user_id:
            user = admin
            break
    if user is None:
        for shopper in Shoppers:
            if shopper.user_id == user_id:
                user = shopper
                break

    if user is None:
        print("User not found.")
        return

    # Start a loop for updating user fields
    while True:
        print("Select a field to update:")
        print("1. Name")
        print("2. Date of Birth")
        print("3. Role")
        print("4. Active Status")
        if isinstance(user, Shopper):
            print("5. Ready to Order (Shopper)")
        print("Q. Finish updating")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter the new name: ")
            user.name = new_name
        elif choice == '2':
            new_date_of_birth = input("Enter the new date of birth (YYYY-MM-DD): ")
            user.date_of_birth = new_date_of_birth
        elif choice == '3':
            new_role = int(input("Enter the new role (0 for admin, 1 for shopper): "))
            user.role = new_role
        elif choice == '4':
            new_active = int(input("Enter the new active status (0 for not active, 1 for active): "))
            user.active = new_active
        elif choice == '5' and isinstance(user, Shopper):
            new_ready_to_order = int(input("Enter the new ready to order status (0 for not ready, 1 for ready): "))
            user.ready_to_order = new_ready_to_order
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice.")

    print("User updated successfully.")
    user.display_user_info()


def display_all_users():
    # Implement Display all users
    if Admin_only_checking() == 1:
        return

    i=1
    o=1
    for admin in Admins:
        print(f"__________Admin number:{i} information_________")
        admin.display_user_info()
        i+=1
    for shopper in Shoppers:
        print(f"__________shopper number:{o} information_________")
        shopper.display_user_info()
        o+=1

def list_products():
    # Implement List products
    if shopper_admin_checking() == 1:
        return

    choice = input("Please choose what whould you like to see : 1)All products 2)Products with offer 3)Category 4)Name ").lower()
    if choice == "1":
        i=1
        for product in products:
            print(f"_______product {i} information______")
            product.display_product_info()
            i+=1
    elif choice == "2":
        b = 1
        for product in products:
                if product.has_offer == '0':
                    pass
                else:

                    print(f"_______product {b} information______")
                    product.display_product_info()
                    b+=1
    elif choice =="3":
        categoryNAME =input("PLease enter the category name you want to display its product :")
        c = 1
        for product in products:
            if product.category== categoryNAME:

                print(f"_______product {c} information______")
                product.display_product_info()
                c+=1
            else :
                pass
    elif choice =="4":
        NAME =input("PLease enter the name of the product you want to display  :")
        a = 1
        for product in products:
            if product.name == NAME:
                print(f"_______product {a} information______")
                product.display_product_info()
                a+=1
            else :
                pass
    else :
        print("invalid choice, please choose 1-2-3-4")







def list_shoppers():
    # Implement List shoppers
    if Admin_only_checking() == 1:
        return

    print("Select a criteria to list shoppers:")
    print("1. All")
    print("2. With items in the basket")
    print("3. Has unprocessed orders")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Listing all shoppers:")
        for shopper in Shoppers:
            shopper.display_user_info()
    elif choice == '2':
        print("Listing shoppers with items in the basket:")
        for shopper in Shoppers:
            if shopper.basket:
                shopper.display_user_info()
    elif choice == '3':
        print("Listing shoppers with unprocessed orders:")
        for shopper in Shoppers:
            if shopper.ready_to_order == 1:
                shopper.display_user_info()
    else:
        print("Invalid choice. Please try again.")




def add_product_to_basket():
    # Implement Add product to the basket
    if shopper_only_checking() == 1:
        return

    user_id = input("Enter your user ID (6 digits only): ")
    if not user_id.isdigit() or len(user_id) != 6:
        print("Invalid user ID. Please enter a 6-digit user ID.")
        return

    shopper = None

    # Find the shopper based on their user ID
    for s in Shoppers:
        if s.user_id == user_id:
            shopper = s
            break

    if not shopper:
        print("Shopper not found.")
        return

    product_id = input("Enter the product ID to add to your basket (6 digits only): ")
    if not product_id.isdigit() or len(product_id) != 6:
        print("Invalid product ID. Please enter a 6-digit product ID.")
        return

    quantity = input("Enter the quantity: ")

    # Check if the product ID exists in the list of products
    product = None
    for p in products:
        if p.product_id == product_id:
            product = p
            break

    if not product:
        print("Product not found.")
        return

    # Add the product and quantity to the shopper's basket
    shopper.add_to_basket(product_id, quantity)
    print(f"Product '{product.name}' added to your basket with quantity {quantity}.")

    # Ask if the shopper wants to save changes to the product.txt file
    save_changes = input("Do you want to save changes to the product list? (yes/no): ").lower()

    if save_changes == "yes":
        save_products_to_file()



def display_basket():
    if shopper_only_checking() == 1:
        return

    user_id = input("Enter your user ID (6 digits only): ")

    # Validate user ID length
    if len(user_id) != 6 or not user_id.isdigit():
        print("Invalid user ID format. Please enter 6 digits only.")
        return

    # Find the shopper based on the user ID
    shopper = None
    for user in Shoppers:
        if user.user_id == user_id:
            shopper = user
            break

    if shopper is None:
        print("User not found.")
        return

    print("Your Basket:")
    total_cost = 0

    for product_id, quantity in shopper.basket.items():
        # Validate product ID length
        if len(product_id) != 6 or not product_id.isdigit():
            print(f"Invalid product ID format: {product_id}. Skipping this item.")
            continue

        # Find the product based on the product ID
        product = None
        for p in products:
            if p.product_id == str(product_id):
                product = p
                break

        if product is not None:
            item_cost = product.price * quantity
            total_cost += item_cost

            print(f"Product ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Price: ${product.price}")
            print(f"Quantity: {quantity}")
            print(f"Item Cost: ${item_cost:.2f}")
            print("----------------------------")

    print(f"Total Cost of Items in Basket: ${total_cost:.2f}")



def update_basket():
    if shopper_only_checking() == 1:
        return

    user_id = input("Enter your user ID (6 digits only): ")

    # Validate user ID length
    if len(user_id) != 6 or not user_id.isdigit():
        print("Invalid user ID format. Please enter 6 digits only.")
        return

    # Find the shopper based on the user ID
    shopper = None
    for user in Shoppers:
        if user.user_id == user_id:
            shopper = user
            break

    if shopper is None:
        print("User not found.")
        return

    while True:
        print("Current Basket:")
        total_cost = 0

        for product_id, quantity in shopper.basket.items():
            # Validate product ID length
            if len(product_id) != 6 or not product_id.isdigit():
                print(f"Invalid product ID format: {product_id}. Skipping this item.")
                continue

            # Find the product based on the product ID
            product = None
            for p in products:
                if p.product_id == str(product_id):
                    product = p
                    break

            if product is not None:
                item_cost = product.price * quantity
                total_cost += item_cost

                print(f"Product ID: {product.product_id}")
                print(f"Name: {product.name}")
                print(f"Price: ${product.price}")
                print(f"Quantity: {quantity}")
                print(f"Item Cost: ${item_cost:.2f}")
                print("----------------------------")

        print(f"Total Cost of Items in Basket: ${total_cost:.2f}")

        # Ask the shopper what action they want to perform
        action = input("Choose an action (clear/remove/update/quit): ").lower()

        if action.lower() == "clear":
            shopper.basket.clear()
            print("Basket cleared.")
        elif action.lower() == "remove":
            product_id = input("Enter the product ID to remove: ")
            # Validate product ID length
            if len(product_id) != 6 or not product_id.isdigit():
                print("Invalid product ID format. Please enter 6 digits only.")
            else:
                if product_id in shopper.basket:
                    del shopper.basket[product_id]
                    print("Product removed from the basket.")
                else:
                    print("Product not found in the basket.")
        elif action.lower() == "update":
            product_id = input("Enter the product ID to update: ")
            # Validate product ID length
            if len(product_id) != 6 or not product_id.isdigit():
                print("Invalid product ID format. Please enter 6 digits only.")
            else:
                if product_id in shopper.basket:
                    new_quantity = int(input("Enter the new quantity: "))
                    if new_quantity > 0:
                        shopper.basket[product_id] = new_quantity
                        print("Basket updated.")
                    else:
                        print("Quantity must be greater than 0.")
                else:
                    print("Product not found in the basket.")
        elif action.lower() == "quit":
            break
        else:
            print("Invalid action. Please choose clear/remove/update/quit.")


def place_order():
    if shopper_only_checking() == 1:
        return

    user_id = input("Enter your user ID (6 digits only): ")

    # Validate user ID length
    if len(user_id) != 6 or not user_id.isdigit():
        print("Invalid user ID format. Please enter 6 digits only.")
        return

    # Find the shopper based on the user ID
    shopper = None
    for user in Shoppers:
        if user.user_id == user_id:
            shopper = user
            break

    if shopper is None:
        print("User not found.")
        return

    order = int(input("Enter the order status (0 for not processed, 1 for processed): "))

    # Validate order value
    if order != 0 and order != 1:
        print("Invalid order status. Please enter 0 for not processed or 1 for processed.")
        return

    shopper.order = order
    print("Order status updated.")


def execute_order():
    # Check if the user is an admin
    if Admin_only_checking() == 1:
        return

    # Ask the admin to enter the user ID of the shopper whose order they want to execute
    shopper_id = input("Enter the user ID of the shopper whose order you want to execute (6 digits only): ")

    # Find the shopper based on the provided ID
    shopper = None
    for s in Shoppers:
        if s.user_id == shopper_id:
            shopper = s
            break

    if shopper is None:
        print("Shopper not found or invalid user ID.")
        return

    # Check if the shopper has items in their basket
    if not shopper.basket:
        print("Shopper's basket is empty. No order to execute.")
        return

    # Process the order
    for product_id, quantity in shopper.basket.items():
        for product in products:
            if product.product_id == product_id:
                if product.inventory < quantity:
                    print(f"Insufficient inventory for product '{product.name}' (Product ID: {product_id}). Order not executed.")
                else:
                    # Deduct the items from the product's inventory
                    product.inventory -= quantity

    # Clear the items from the shopper's basket
    shopper.basket.clear()
    print("Order executed successfully. Inventory updated and basket cleared.")

    # Save the updated product information to the file
    save_products_to_file()


def save_products_to_file():
    # Implement Save products to a file
    if Admin_only_checking() == 1:
        return
    i=1
    save_product_file = input("Enter the name of the file you want to save products in: ")
    try:
        with open(save_product_file, "w") as file:
            # Write the product information to the file
            for product in products:
                file.write(f"_________product {i} information________\n")
                file.write(f"Product ID: {product.product_id}\n")
                file.write(f"Product Name: {product.name}\n")
                file.write(f"Product Category: {product.category}\n")
                file.write(f"Price: {product.price}\n")
                file.write(f"Inventory: {product.inventory}\n")
                file.write(f"Supplier: {product.supplier}\n")
                file.write(f"Has an Offer: {'Yes' if product.has_offer=='1' else 'No'}\n")
                if product.has_offer == '1':
                    file.write(f"Offer Price: {product.offer_price}\n")
                    file.write(f"Valid Until: {product.valid_until}\n")
                file.write("\n")
                i+=1

        print(f"Products saved to '{save_product_file}' successfully.")
    except Exception as e:
        print(f"An error occurred while saving products: {str(e)}")




def save_users_to_text_file():
    # Check if the user is an admin
    if Admin_only_checking() == 1:
        return

    # Ask the admin to input the name of the text file
    file_name = input("Enter the name of the text file to save users (e.g., users.txt): ")

    try:
        with open(file_name, "w") as file:
            # Write user information to the file
            for user in Admins + Shoppers:
                user_data = f"{user.user_id};{user.name};{user.date_of_birth};{user.role};{user.active}"

                if isinstance(user, Shopper):
                    user_data += f";{user.ready_to_order}"
                    if user.basket:
                        basket_data = ';'.join([f"{product_id}:{quantity}" for product_id, quantity in user.basket.items()])
                        user_data += ';' + basket_data

                file.write(user_data + "\n")

        print(f"Users saved to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred while saving users: {str(e)}")


def exit_program():
    # Ask the user to save products and users if they haven't already
    save_products_response = input("Do you want to save products before exiting? (yes/no): ").lower()
    if save_products_response == "yes":
        save_products_to_file()

    save_users_response = input("Do you want to save users before exiting? (yes/no): ").lower()
    if save_users_response == "yes":
        save_users_to_text_file()

    print("Exiting the system.")
    exit()

if __name__ == "__main__":
    store = OnlineStore()

   #loading the products
    with open("products.txt", "r") as file:
        for line in file:
            product = Product.from_text(line)
            products.append(product)

    # Example: Print information for all loaded products
    for product in products:
       product.display_product_info()

   #loading the users
    # --------------------------------------------------------------------------



    with open("users.txt", "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace, including the newline character
            data = line.split(";")
            role = int(data[3]) # Assuming role is the 4th element
            if role == 0 :

                Admins.append(Admin(*data))
            else:
                if len(data) > 6:
                    Shoppers.append(Shopper(*data))
                else:
                    Shoppers.append(Shopper(*data))

        # Display information for admin users
       # for admin in Admins:
        #      admin.display_user_info()
    # Display information for shopper users
        #for shopper in Shoppers:
         #  shopper.display_user_info()
    # --------------------------------------------------------------------------------------------

    while True:
        print("\nMenu Options:")
        print("1. Add product (admin-only)")
        print("2. Place an item on sale (admin-only)")
        print("3. Update product (admin-only)")
        print("4. Add a new user (admin-only)")
        print("5. Update user (admin-only)")
        print("6. Display all users (admin-only)")
        print("7. List products (admin and shopper)")
        print("8. List shoppers (admin)")
        print("9. Add product to the basket (shopper-only)")
        print("10. Display basket (shopper-only)")
        print("11. Update basket (shopper-only)")
        print("12. Place order (shopper-only)")
        print("13. Execute order (admin-only)")
        print("14. Save products to a file (admin-only)")
        print("15. Save users to a text file (admin-only)")
        print("16. Exit")

        choice = input("Enter your choice: ")

        menu_actions = {
            '1': add_product,
            '2': place_item_on_sale,
            '3': update_product,
            '4': add_new_user,
            '5': update_user,
            '6': display_all_users,
            '7': list_products,
            '8': list_shoppers,
            '9': add_product_to_basket,
            '10': display_basket,
            '11': update_basket,
            '12': place_order,
            '13': execute_order,
            '14': save_products_to_file,
            '15': save_users_to_text_file,
            '16': exit_program,
        }

        selected_action = menu_actions.get(choice)
        if selected_action:
            selected_action()
        else:
            print("Invalid choice. Please try again.")
