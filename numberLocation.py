import phonenumbers
from myNumber import number
from phonenumbers import geocoder
import folium

key = '2ef0cb1afd864632843a41fa6918ebbe'
samNum = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNum, "en")
print(yourLocation)
from phonenumbers import carrier

service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
query = str(yourLocation)
res = geocoder.geocode(query)
# print(res)
lat = res[0]['geometry']['lat']
lng = res[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start= 9)

folium.Marker([lat,lng], popup= yourLocation).add_to((myMap))

myMap.save("myLocation.html")
