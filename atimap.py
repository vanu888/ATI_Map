# Import  folium  libary
import folium

# Create a map object
m = folium.Map(location=[7.8731, 80.7718], zoom_start=8)

# Add markers to the map
folium.Marker(
    location=[7.29087222590764, 80.63401499844234],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Kandy"
    
).add_to(m)

folium.Marker(
    location=[6.92384148500146, 79.86178503298707],
    icon=folium.Icon(color="red"),
    tooltip="ATI- Colombo"
    
).add_to(m)

folium.Marker(
    location=[6.9944146379762895, 81.06298902604381],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Badulla"
    
).add_to(m)

folium.Marker(
    location=[8.600030054815146, 81.19328895848626],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Trincomalee"
    
).add_to(m)

folium.Marker(
    location=[6.074191186816379, 80.23333978611325],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Galle"
    
).add_to(m)

folium.Marker(
    location=[7.247335487904954, 80.35707302746803],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Kegalle"
    
).add_to(m)

folium.Marker(
    location=[7.27972352808466, 81.65294613641184],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Ampara-Hardy"
    
).add_to(m)

folium.Marker(
    location=[6.856641872643731, 79.86811630755396],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Dehiwala"
    
).add_to(m)

folium.Marker(
    location=[7.166504818398097, 80.0363792857597],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Gampaha"
    
).add_to(m)

folium.Marker(
    location=[9.651811316790111, 80.02352876368222],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Jaffna"
    
).add_to(m)

folium.Marker(
    location=[7.486101197566701, 80.35342316741365],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Kurunagala"
    
).add_to(m)

folium.Marker(
    location=[6.709176101328276, 80.37996619677621],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Rathnapura"
    
).add_to(m)

folium.Marker(
    location=[7.353798196055019, 81.78136255591225],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Samamanthurai"
    
).add_to(m)

folium.Marker(
    location=[6.056245240523357, 80.82700140547824],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Tangalle"
    
).add_to(m)

folium.Marker(
    location=[8.848098748609262, 80.49671467073246],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Vauniya"
    
).add_to(m)

folium.Marker(
    location=[7.027232822722302, 80.53548779246982],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Nawalapitiya"
    
).add_to(m)

folium.Marker(
    location=[8.889941335018184, 79.99496088592723],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Mannar"
    
).add_to(m)

folium.Marker(
    location=[8.325318795978706, 80.36780072989485],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Anuradhapura"
    
).add_to(m)

folium.Marker(
    location=[7.6576747227337325, 81.74107244461628],
    icon=folium.Icon(color="green"),
    tooltip="ATI- Batticaloa"
    
).add_to(m)


# Save  the map as an HTML file
m.save("ATI-map.html")