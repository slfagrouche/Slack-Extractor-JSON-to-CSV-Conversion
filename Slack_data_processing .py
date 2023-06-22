import csv
import json
import re

# Read JSON file
with open('Slack export Jan 21 2020 - May 21 2023/ai-ml-xr/2020-07-26.json', 'r') as file:
    data = json.load(file)

# Initialize lists for extracted information
links = []
image_links = []
text = []

# Extract information from each message
for message in data:
    if 'text' in message:
        if "has joined the group" not in message['text']:  # Exclude "has joined the group" messages
            # Extract links from the message text
            urls = re.findall(r'(https?://\S+)', message['text'])
            for url in urls:
                if url.endswith(('png', 'jpg', 'jpeg', 'gif')):
                    image_links.append(url)
                else:
                    links.append(url)
            
            # Extract text from the message
            text.append(message['text'])
    
    if 'user_profile' in message:
        # Extract icon from the user profile
        image_links.append(message['user_profile']['image_72'])

# Create a list of dictionaries for each message
messages = []
for i in range(len(text)):
    message = {
        'text': text[i],
        'links': links[i] if i < len(links) else '',
        'image_links': image_links[i] if i < len(image_links) else ''
    }
    messages.append(message)

# Define field names for CSV
fieldnames = ['text', 'links', 'image_links']

# Save extracted information to a CSV file
with open('extracted_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(messages)
