country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.


def add_new_country(country: str, visits: int,
                    list_of_cities: list[str]) -> None:
    new_log = {
        'country': country,
        'visits': visits,
        'cities': list_of_cities
    }
    travel_log.append(new_log)

    # Test to order by num of visits:
    # travel_log.sort(key=lambda x: x['visits'], reverse=False)
    # print(travel_log)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(
    f"I've been to {travel_log[2]['country']} "
    f"{travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
