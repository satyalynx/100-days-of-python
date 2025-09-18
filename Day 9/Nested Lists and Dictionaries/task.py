capitals = {
    "france": "Paris",
    "Germany": "Berlin",
}

#Nested list in dictionary

#travel_log = {
#    "France": ["Paris", "Lists", "Dijon"],
#    "Germany": ["Stuttgart", "Berlin"],
#}

#print lille
#print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])

#dictionary within a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lists", "Dijon"],
        "total_visited": 12
    },
    "Germany": {
        "cities_visited": ["hamburg", "Stuttgart", "Berlin"],
        "total_visits": 5
        },
    }

    print(travel_log["Germany"]["cities_visited"][2])