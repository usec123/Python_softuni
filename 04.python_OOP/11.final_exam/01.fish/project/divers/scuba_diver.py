from .base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        super().miss(round(0.3*time_to_catch))

    def renew_oxy(self):
        self.oxygen_level = self.starting_oxygen
