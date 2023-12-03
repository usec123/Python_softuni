from .computer import Computer


class Laptop(Computer):
    VALID_RAM_SIZES = {size: Computer.VALID_RAM_SIZES[size] for size in list(Computer.VALID_RAM_SIZES.keys())[:-1:]}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        processors = {'AMD Ryzen 9 5950X': 900, 'Intel Core i9-11900H': 1050, 'Apple M1 Pro': 1200}
        if processor not in processors:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')
        if ram not in self.VALID_RAM_SIZES:
            raise ValueError(f'{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!')

        self.price += processors[processor]
        self.processor = processor
        self.price += self.VALID_RAM_SIZES[ram]
        self.ram = ram

        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
