import json
import sys

# How to use:
# Place the script in the same directory as the file you want to convert
# In the terminal use the format below:
# python3 convert-JSON-to-JSONL.py nameOfYourInputFile.json nameOfTheNewConvertedFile.json

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    json_data = json.load(f)
    
with open(output_file, 'w') as outfile:
    for entry in json_data:
        json.dump(entry, outfile)
        outfile.write('\n')