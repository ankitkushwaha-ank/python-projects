def get_location():
    try:
        # Using ipinfo.io to get location data
        response = requests.get('https://ipinfo.io')
        data = response.json()

        # Extract location details
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        loc = data.get('loc')  # Latitude and Longitude

        print(f"Location: {city}, {region}, {country}")
        print(f"Coordinates: {loc}")

    except Exception as e:
        print(f"Error: {e}")


if get_location == "_main_":
    get_location()