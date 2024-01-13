from .computer import Computer


class DesktopComputer(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        processors = {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}
        if processor not in processors:
            raise ValueError(f'{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!')

        if ram not in self.VALID_RAM_SIZES:
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!')

        self.price += processors[processor]
        self.processor = processor
        self.price += self.VALID_RAM_SIZES[ram]
        self.ram = ram

        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
