import requests 

base_url = 'https://api.github.com/'

# add access token
# still figuring this out
access_token = ''
property_id = 'your property id'

headers = {
	'Authorization': f'Bearer {access_token}',
	'Content-Type': 'application/json'
}

reservation_url = f'{base_url}/booking/v1/reservations?propertyIds={property_id}'
response = requests.get(reservation_url, headers=headers)

if response.status_code == 200:
	reservations = response.json()
	print(reservations)
else:
	print(f"Error: {response.status_code} - {response.text}")
	print(response)
