# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.


def city_country(city, country):

  location = city.title() + ',' + country.title()
  return location

geo = city_country('santiago', 'chile')
print(geo)


    