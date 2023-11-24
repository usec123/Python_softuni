from .customer import Customer
from .dvd import DVD


class MovieWorld:
    dvds_capacity = 15
    customers_capacity = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.dvds_capacity

    @staticmethod
    def customer_capacity():
        return MovieWorld.customers_capacity

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customers_capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvds_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f'{customer.name} has already rented {dvd.name}'
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            return 'DVD is already rented'
                        if customer.age < dvd.age_restriction:
                            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        self.dvds.append(customer.rented_dvds.pop(customer.rented_dvds.index(dvd)))
                        dvd.is_rented = False
                        return f'{customer.name} has successfully returned {dvd.name}'
                return f'{customer.name} does not have that DVD'

    def __repr__(self):
        return '\n'.join([str(person) for person in self.customers] + [str(dvd) for dvd in self.dvds])
