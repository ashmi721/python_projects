from geopy.geocoders import Nominatim

# Create the geolocator object with a modified user-agent for English language
geolocator = Nominatim(user_agent='getaddress (English)')

# Get the city name from the user
address = input("Enter city name: ")

# Geocode the location
location = geolocator.geocode(address)


# Print the geolocation details
print(location)
