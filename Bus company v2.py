class Bus:
    bus_list = []

    def __init__(self, number, route_key, driver):
        self.number = number
        self.route_key = route_key
        self.driver = driver
        Bus.bus_list.append(self)

    def display_info(self):
        for bus in Bus.bus_list:
            if bus == self
                print(f"Bus number = {bus.number} "
                      f"on route {bus.route_key} "
                      f"with driver {bus.driver}")


bus1 = Bus("2010", "Y", "Greg")
bus2 = Bus("2011", "P", "Bob")
bus3 = Bus("2012", "130", "Bob")

# print information
for bus in range(len(Bus.bus_list)):
    Bus.display_info(Bus.bus_list[bus])
