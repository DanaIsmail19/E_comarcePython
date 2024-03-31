class Admin:
    def __init__(self, user_id, name,date_of_birth,role,active):
        self.user_id = user_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.role = role  # 0 for admin, 1 for shopper
        self.active = active



    # this is for printing after loading
    def display_user_info(self):

        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Role: {'Admin' }")
        print(f"Active: {'Yes' if self.active == 1 else 'No'}")

        print("-----------------------------------------------------")


