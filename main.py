# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions

#Example 1

# cities_in_F = {'Tashkent': 32, 'Samarkand': 75, 'Nukus': 100, 'Mangit': 50}
#
# cities_in_C = {key: round((value)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)

#Example 2

# weather = {'Tashkent': "snowing", 'Samarkand': 'sunny', 'Nukus': 'sunny', 'Mangit': 'cloudy'}
#
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)

#Example 3

cities = {'Tashkent': 32, 'Samarkand': 75, 'Nukus': 100, 'Mangit': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(desc_cities)