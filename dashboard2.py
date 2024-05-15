import solara_sdk

# Assuming you have authentication credentials configured
client = solara_sdk.Client(api_key='YOUR_API_KEY')

# Assuming you already have the dashboard ID
dashboard_id = 'YOUR_DASHBOARD_ID'

# Define the title you want to add to the dashboard
title_text = 'My Dashboard Title'

# Add the title widget to the dashboard
widget = {
    'type': 'text',
    'text': title_text,
    'position': {
        'x': 0,
        'y': 0,
        'width': 4,
        'height': 1
    }
}

# Send a request to Solara API to add the title widget to the dashboard
response = client.update_dashboard(dashboard_id, widgets=[widget])

# Check if the request was successful
if response['status'] == 'success':
    print('Title added successfully.')
else:
    print('Failed to add title:', response['message'])
