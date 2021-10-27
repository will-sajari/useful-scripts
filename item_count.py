import json
import csv
from collections import Counter


# This script will take a JSON file and output a CSV with two columns.
# Column A is a unique value of the item you want to count.
# Column B is the count.

input_filename = "name_of_your_file.json"

with open(input_filename) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

# Set an empty list, we will add ALL values you want to count here. Name this anything you like
all_items = []

# Loop through your list and add to the list above
# Edit this to get the values you want
for item in jsonObject:
    if "thing_im_looking_for" in item:
        all_items.extend(item["thing_im_looking_for"])

# Counter will count all occurrances and return a dictionary of counts
total_images = Counter(all_items)

# Write this to a CSV
output_filename = "total_count.csv"

with open(output_filename, 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in total_images.items():
       writer.writerow([key, value])