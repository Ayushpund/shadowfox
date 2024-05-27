city_country_map = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}

def find_country(city_name):
    for city, country in city_country_map.items():
        if city_name.lower() == city.lower():
            return country
    return None

def are_same_country(city1, city2):
    country1 = find_country(city1)
    country2 = find_country(city2)
    if country1 and country2:
        return country1 == country2
    else:
        return False

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if are_same_country(city1, city2):
    print("Both cities are in the same country")
else:
    print("They don't belong to the same country")
