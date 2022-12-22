import pandas as pd
import copy


df = pd.read_csv('pokemon_status.csv', encoding = 'shift_jis')
data = df['ポケモン名'].values
pokemon = []
for i in data:
    if len(i) == 5:
        pokemon.append(i)

while True:
    s, hitbrow = input("=> ").split()
    l_hitbrow = list(hitbrow)
    blow = []
    hit = []
    for index, i in enumerate(l_hitbrow):
        if int(i) == 1:
            hit.append(s[index])
        else:
            hit.append(0)
        if int(i) == 2:
            blow.append(s[index])
        else:
            blow.append(0)
    for index, i in enumerate(pokemon):
        for j in range(len(blow)):
            if blow[j] == 0 and hit[j] == 0:
                if s[j] in i and s.count(s[j]) == 1:
                    pokemon[index] = "None"
            if hit[j] != 0:
                if s[j] != i[j]:
                    pokemon[index] = "None"
            else:
                if s[j] == i[j]:
                    pokemon[index] = "None"
            if blow[j] != 0:
                if not(s[j] in i):
                    pokemon[index] = "None"
    pokemon2 = []
    count = 0
    for i in pokemon:
        if i != "None":
            pokemon2.append(i)
    pokemon = copy.copy(pokemon2)
    print(*pokemon)
    if len(pokemon) <= 1:
        break