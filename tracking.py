import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

key = 'a43cb997ca51413882ea52c42f9bf4de' # Replace with your actual OpenCage API key
# Input the phone number you want to track
number = input("Enter the phone number with country code (e.g., +9779812345678): ")
#this will provie the location of the number where it is registered
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print("Location:", number_location)
# this will provide the information about carrier (i.e service provider for eg. Ncell, Ntc, etc.)
number_carrier = carrier.name_for_number(check_number, "en")
print("Carrier:", number_carrier)

# this will provide the coordinates of the number
geocoder = OpenCageGeocode(key) # Initialize OpenCageGeocode with your API key
query = str(number_location)  # Convert location to string for geocoding
results = geocoder.geocode(query) # Check if results are found
if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Coordinates:", lat, lng)
else:
    print("No results found for the location.")
# Create a map centered at the coordinates
map_location = folium.Map(location=[lat, lng], zoom_start=10) 
# Add a marker for the location
folium.Marker([lat, lng], popup=number_location).add_to(map_location) 
# Save the map to an HTML file
map_location.save("location_map.html")