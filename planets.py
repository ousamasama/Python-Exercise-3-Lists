planet_list = ["Mercury", "Mars"]
# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)
# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list2 = ["Uranus", "Neptune"]
planet_list.extend(planet_list2)
print("Added two planets", planet_list)
# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(2, "Venus")
planet_list.insert(3, "Earth")
print("Planets in order", planet_list)
# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print("Pluto added", planet_list)
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = slice(4)
print("Rockey Planets", planet_list[rocky_planets])
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print("Plutoless list", planet_list)

#challenge
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
space_missions = (('Rover', 'Mars'), ('Cassini', 'Saturn'), ('Lucy', 'Jupiter'))
# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
    for planet_visited in space_missions:
        # print("planet_list", a)
        # print("space_missions", b[1])
        if planet_visited[1] == planet:
            print(f"{planet_visited[0]} visited {planet}.")