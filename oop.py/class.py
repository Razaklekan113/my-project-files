class user:
    def log(self):
        print("User logged")

class Customer(user):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name


    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type
    
    def print_all_customer(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    
    __hash__ = None

    __repr__ = __str__

customer = [Customer("razak", "gold"),
            Customer("Abiola", "silver")]


print("Before update:")
print(customer[0])
print(customer[1])
print()

print("After update:")
customer[0].update_membership("Siver")
customer[1].update_membership("Bronze")

print(customer[0])
print(customer[1])
print()

print("Printing all customer:")
Customer.print_all_customer(customer)
print()

print("Checking customer equivalent:")
print(customer[0]==customer[1])
print()

print("Customers:")
print(customer)

customer[0].log