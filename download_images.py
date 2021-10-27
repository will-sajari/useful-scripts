# This script was adapted from https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
import requests # to get image from the web
import shutil # to save it locally
import json

input_file = "name_of_your_file.json"

with open(input_file) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

for product in jsonObject:
    if "images_list" in product:
        for image_url in product["images_list"]:
            ## Set up the image URL and filename
            filename = image_url.split("/")[-1]

            # Open the url image, set stream to True, this will return the stream content.
            r = requests.get(image_url, stream = True)

            # Check if the image was retrieved successfully
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
                
                # Open a local file with wb ( write binary ) permission.
                with open(f"./data/images/{filename}",'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    
                print('Image sucessfully Downloaded: ',filename)
            else:
                print('Image Couldn\'t be retreived')

