class Bus:
    def __init__(self, number, route_key, driver):
        self.number = number
        self.route_key = route_key
        self.driver = driver

    def print_details(self):
        return f"Bus number: {self.number}\nRoute Key: {self.route_key}\n" \
               f"Driver: {self.driver}\n"


bus1 = Bus("2010", "Y", "Greg")
bus2 = Bus("2011", "P", "Bob")
bus3 = Bus("2012", "130", "Bob")

print(Bus.print_details(bus1))
print(Bus.print_details(bus2))
print(Bus.print_details(bus3))
