class Product:
    def __init__(self, product_id, name, category, price, inventory, supplier,
                 has_offer, offer_price=None, valid_until=None):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.inventory = inventory  #number of item avilable
        self.supplier = supplier
        self.has_offer = has_offer    #1 has offer , 0 not
        self.offer_price = offer_price
        self.valid_until = valid_until  # the date to the offer to end


    #for printing only
    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price}")
        print(f"Inventory: {self.inventory} units")
        print(f"Supplier: {self.supplier}")

        if self.has_offer=='1':
            print(f"Offer Price: ${self.offer_price}")
            print(f"Offer Valid Until: {self.valid_until}")
        else:
            print("No current offer on this product")
        print("-----------------------------------------------------")
    # this is for loading purposes
    @classmethod
    def from_text(cls, text):
            data = text.strip().split(';')
            product_id, name, category, price, inventory, supplier, has_offer, offer_price, valid_until = data
            if has_offer =='1':
                offer_price = float(offer_price)
                valid_until = valid_until
            else:
                offer_price = None
                valid_until = None

            return cls(product_id, name, category, float(price), int(inventory), supplier,
                       has_offer, offer_price, valid_until)
