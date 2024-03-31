from Admin import Admin


class Shopper(Admin):
    def __init__(self, user_id, name,date_of_birth, role, active, ready_to_order, *basket_data):
        super().__init__(user_id, name, date_of_birth, role, active)
        self.ready_to_order = ready_to_order  # Default value for ready_to_order is True
        self.basket = {}

        if basket_data:  # Check if basket data is available
            for item in basket_data:
                parts = item.split(':')
                if len(parts) == 2:
                    product_id, quantity = parts
                    self.basket[int(product_id)] = int(quantity)

    #user_id;name;date_of_birth;role;active;ready_to_order;basket_data



    # this is for printing after loading
    def display_user_info(self):

        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Role: {'Shopper'}")
        print(f"Active: {'Yes' if self.active == 1 else 'No'}")
        print(f"Ready to Order: {'Yes' if self.ready_to_order else 'No'}")
        print("Basket:")
        for product_id, quantity in self.basket.items():
            print(f"  Product ID: {product_id}, Quantity: {quantity}")
        print("-----------------------------------------------------")



    def add_to_basket(self, product_id, quantity):
            # Check if the product_id already exists in the basket
            if product_id in self.basket:
                # If it exists, update the quantity
                self.basket[product_id] += int(quantity)
            else:
                # If it doesn't exist, add it to the basket with the given quantity
                self.basket[product_id] = int(quantity)
