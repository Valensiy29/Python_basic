players = {

    ("Ivan", "Volkin"): (10, 5, 13),

    ("Bob", "Robbin"): (7, 5, 14),

    ("Rob", "Bobbin"): (12, 8, 2)

}
spis = []
for pep,val in players.items():
    pep += val
    spis.append((pep))
print(spis)

