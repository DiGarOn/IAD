votes = open("input.txt", "r", encoding="utf-8")
parties = {}
overall_votes = 0

for line in votes:
    elements = line.split()[::-1]
    number_of_votes = elements[0]
    overall_votes += int(number_of_votes)

    elements = elements[::-1]
    party = " ".join(elements[0:len(elements) - 1])

    parties[party] = parties.get(party, 0) + int(number_of_votes)


# calculating “первое избирательное частное”:
pervoe_izb_chastnoe = overall_votes / 450


# calculating the number of seats in the parliament for each party:
seats = {}
all_mandates = 0
fraction = {}

for party in parties.items():
    number_of_seats = int(party[1] / pervoe_izb_chastnoe)
    seats[party[0]] = seats.get(party[0], 0) + number_of_seats

    # creating a dict with fraction parts
    fraction[party[0]] = fraction.get(party[0], 0) + (party[1] / pervoe_izb_chastnoe - number_of_seats)

    # keeping track of all mandates
    all_mandates += number_of_seats

# sorted fraction part
sorted_fraction = sorted(fraction.items(), key=lambda x: -x[1])

while all_mandates < 450:
    index_i = 0
    for index_j in range(1, len(sorted_fraction)):
        if (sorted_fraction[index_j][1] == sorted_fraction[index_i][1]) and (parties[sorted_fraction[index_j][0]] > parties[sorted_fraction[index_i][0]]):
            index_i = index_j

    all_mandates += 1
    seats[sorted_fraction[index_i][0]] += 1

for party in seats.items():
    print(party[0], party[1])