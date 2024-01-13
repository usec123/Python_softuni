def team_lineup(*args):
    output = ''
    team = {} # player - country
    countries_participants = {}
    for x in args:
        team[x[0]] = x[1]
    for country in team.values():
        countries_participants[country] = list(team.values()).count(country)
    countries_participants = dict(sorted(countries_participants.items(), key=lambda x: (-x[1],x[0])))
    for key in countries_participants:
        output+=f'{key}:\n'
        for x in team:
            if team[x] == key:
                output+=f'  -{x}\n'
    return output
    

print(team_lineup(

("Harry Kane", "England"),

("Manuel Neuer", "Germany"),

("Raheem Sterling", "England"),

("Toni Kroos", "Germany"),

("Cristiano Ronaldo", "Portugal"),

("Thomas Muller", "Germany")))

print('---------------------------------')

print(team_lineup(

("Lionel Messi", "Argentina"),

("Neymar", "Brazil"),

("Cristiano Ronaldo", "Portugal"),

("Harry Kane", "England"),

("Kylian Mbappe", "France"),

("Raheem Sterling", "England")))

print('---------------------------------')

print(team_lineup(

("Harry Kane", "England"),

("Manuel Neuer", "Germany"),

("Raheem Sterling", "England"),

("Toni Kroos", "Germany"),

("Cristiano Ronaldo", "Portugal"),

("Thomas Muller", "Germany"),

("Bruno Fernandes", "Portugal"),

("Bernardo Silva", "Portugal"),

("Harry Maguire", "England")))