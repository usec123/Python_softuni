from divers.free_diver import BaseDiver, FreeDiver
from divers.scuba_diver import ScubaDiver
from fish.deep_sea_fish import BaseFish, DeepSeaFish
from fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        mapper = {
            'FreeDiver': FreeDiver,
            'ScubaDiver': ScubaDiver
        }
        if diver_type not in mapper:
            return f"{diver_type} is not allowed in our competition."
        if diver_name in [diver.name for diver in self.divers]:
            return f"{diver_name} is already a participant."
        self.divers.append(mapper[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        mapper = {
            'PredatoryFish': PredatoryFish,
            'DeepSeaFish': DeepSeaFish
        }
        if fish_type not in mapper:
            return f'{fish_type} is forbidden for chasing in our competition.'
        if fish_name in [fish.name for fish in self.fish_list]:
            return f"{fish_name} is already permitted."
        self.fish_list.append(mapper[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        if diver_name not in [diver.name for diver in self.divers]:
            return f'{diver_name} is not registered for the competition.'
        diver: BaseDiver = [diver for diver in self.divers if diver.name == diver_name][0]

        if fish_name not in [fish.name for fish in self.fish_list]:
            return f'The {fish_name} is not allowed to be caught in this competition.'
        fish: BaseFish = [fish for fish in self.fish_list if fish.name == fish_name][0]

        if diver.has_health_issues:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issues:
                diver.update_health_status()
                diver.oxygen_level = diver.starting_oxygen
                count += 1
        return f'Divers recovered: {count}'

    def diver_catch_report(self, diver_name: str):
        if diver_name in [diver.name for diver in self.divers]:
            diver: BaseDiver = [diver for diver in self.divers if diver.name == diver_name][0]
            return (f'**{diver.name} Catch Report**\n'
                    f'{"\n".join(fish.fish_details() for fish in tuple(diver.catch))}')

    def competition_statistics(self):
        divers = sorted([diver for diver in self.divers if not diver.has_health_issues],
                        key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        return ('**Nautical Catch Challenge Statistics**\n'
                f'{"\n".join([str(diver) for diver in divers])}')
