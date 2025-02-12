populations = [
    [106,107,111,133,221,767,1766],
    [502,635,809,947,1402,3634,5268],
    [2,2,2,6,13,30,46],
    [163,203,276,408,547,729,628],
    [2,7,26,82,172,307,392],
    [16,24,38,74,167,511,809]
]
continents = [
    "Africa",
    "Asia",
    "Australia",
    "Europe",
    "North America",
    "South America",
    "Totals"
]


headers = print(f"{"Year":<20}{"1750":<10}{"1800":<6}\
    {"1850":<10}{"1900":<10}{"1950":10}{"2000":<6}\
    {"2050":<6}")

for i in range(len(populations)):
    print(f"{continents[i]:<20}", end="")
    for j in range(len(populations[0])):
         print(f"{populations[i][j]: <10}", end="")
    print()

yearly_populations_totals = []
for j in range(len(populations[0])):
    sum = 0 # resets to a new column
    for i in range(len(populations)):
        sum = sum + populations[i][j]
    yearly_populations_totals.append(sum)

populations.append(yearly_populations_totals)

for q in range(1):
    print(f"{continents[6]:<20}", end="")
    for m in range(len(yearly_populations_totals)):
        print(f"{yearly_populations_totals[m]: <10}", end="")
print()


