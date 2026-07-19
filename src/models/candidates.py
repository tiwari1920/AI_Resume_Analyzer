class Candidate:
    def __init__(self, name="", email="", phone=""):
        self.name = name
        self.email = email
        self.phone = phone
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Phone: ", self.phone)

