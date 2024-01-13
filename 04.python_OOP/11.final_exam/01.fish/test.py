from project.nautical_catch_challenge_app import NauticalCatchChallengeApp


nca = NauticalCatchChallengeApp()

print(nca.divers)
print(nca.fish_list)

nca.dive_into_competition('FreeDiver', 'a')
nca.dive_into_competition('ScubaDiver', 'b')

nca.swim_into_competition('DeepSeaFish', 'a', 1)
nca.swim_into_competition('PredatoryFish', 'b', 2)

print(nca.divers)
print(nca.fish_list)

nca.divers[0].has_health_issues = True

print(nca.health_recovery())

print(nca.diver_catch_report('b'))
nca.chase_fish('b', 'a', True)
print([diver for diver in nca.divers if diver.name == 'b'][0].catch)
print(nca.diver_catch_report('b'))
