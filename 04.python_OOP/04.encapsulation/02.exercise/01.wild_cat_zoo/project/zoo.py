from .animal import Animal
from .worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity - len(self.animals) > 0:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_cost = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        def format_text(animal_list):
            return '\n'.join([str(animal) for animal in animal_list])

        return '\n'.join([f'You have {len(self.animals)} animals',
                          f'----- {len(lions)} Lions:',
                          f'{format_text(lions)}',
                          f'----- {len(tigers)} Tigers:',
                          f'{format_text(tigers)}',
                          f'----- {len(cheetahs)} Cheetahs:',
                          f'{format_text(cheetahs)}'
                          ])

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]

        def format_text(worker_list):
            return '\n'.join([str(worker) for worker in worker_list])

        return '\n'.join([f'You have {len(self.workers)} workers',
                          f'----- {len(keepers)} Keepers:',
                          f'{format_text(keepers)}',
                          f'----- {len(caretakers)} Caretakers:',
                          f'{format_text(caretakers)}',
                          f'----- {len(vets)} Vets:',
                          f'{format_text(vets)}'
                          ])
