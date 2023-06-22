# Slack-Data-Processing-in-JSON
### - Extracting Information from Slack Export

This code is designed to extract information from a Slack export JSON file and save the extracted data into a CSV file. The extracted information includes links, image links, and text from each message in the JSON file.

## Prerequisites 
> Python 3.x 
> 
> Slack export JSON file 
## Instructions
Place the Slack export JSON file in the same directory as the Python script.
Modify the script if necessary to match the correct path and filename of the JSON file. Replace 'Slack export Jan 21 2020 - May 21 2023/ai-ml-xr/2020-07-26.json' in line 6 with the correct path and filename.
Run the Python script. It will extract the information from the JSON file and save it to a CSV file named extracted_data.csv.
After running the script, you can find the generated CSV file in the same directory as the Python script.
## Code Explanation
1. The script imports the necessary libraries: csv for CSV file operations, json for reading JSON files, and re for regular expressions.
2. The JSON file is opened and loaded using the json.load() function.
3. Empty lists are initialized to store the extracted information: links for regular links, image_links for image links, and text for message text.
4. The script iterates over each message in the JSON data and checks if the message contains text. It excludes messages containing the phrase "has joined the group".
5. URLs are extracted from the message text using regular expressions. If a URL ends with an image file extension (e.g., 'png', 'jpg', 'jpeg', 'gif'), it is added to the image_links list; otherwise, it is added to the links list.
6. The text of the message is appended to the text list.
7. If a message has a user profile, the script extracts the profile's icon URL and adds it to the image_links list.
8. A list of dictionaries is created, where each dictionary represents a message and contains the text, links, and image links.
9. Field names for the CSV file are defined.
10. The extracted information is written to a CSV file using the csv.DictWriter() and writerows() functions.

Please note that this code assumes the JSON file is formatted correctly and follows the structure expected by the script. Additionally, it assumes the JSON file contains the necessary information for extracting links, image links, and text from each message.

Feel free to modify the code according to your specific needs or integrate it into a larger project.
