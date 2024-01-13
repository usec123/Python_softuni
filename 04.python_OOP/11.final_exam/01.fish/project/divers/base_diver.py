from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    OXYGEN_COEFFICIENT = 1

    @abstractmethod
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.starting_oxygen = oxygen_level
        self.catch = []
        self.competition_points = 0
        self.has_health_issues = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not len(value.replace(' ', '')):
            raise ValueError('Diver name cannot be null or empty!')
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return round(self.__competition_points, 1)

    @competition_points.setter
    def competition_points(self, value):
        self.__competition_points = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        needed_oxygen = time_to_catch
        current_oxygen_level = round(self.oxygen_level - needed_oxygen)
        if current_oxygen_level < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = current_oxygen_level

    @abstractmethod
    def renew_oxy(self):
        self.oxygen_level = self.starting_oxygen

    def hit(self, fish: BaseFish):
        # current_oxygen_level = self.oxygen_level - fish.time_to_catch
        # if current_oxygen_level < 0:
        #     self.oxygen_level = 0
        # if current_oxygen_level >= 0:
        #     self.oxygen_level = current_oxygen_level
        #     self.catch.append(fish)
        #     self.competition_points += round(fish.points, 1)

        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
        else:
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)

    def update_health_status(self):
        self.has_health_issues = not self.has_health_issues

    def __str__(self):
        return (f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]")