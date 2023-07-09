import requests, uuid, json, argparse, sys
import langcodes

# This is for the safety of the key
from config import AZURE_KEY
# Add your key and endpoint
key = AZURE_KEY
endpoint = "https://api.cognitive.microsofttranslator.com"


# Creating an argument parser
parser = argparse.ArgumentParser(description="Tranlate text from one language to another")
parser.add_argument('input_file', help='Path to the input file')
parser.add_argument("-t", "--to", help = "translation language")
args = parser.parse_args()


#getting translation language and input file from arguments
input_file = args.input_file
translation_language = args.to
translation_language_code = langcodes.find(translation_language.lower()).language
with open(input_file, 'r') as file:
    text = file.read()


# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "centralindia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'to': [translation_language_code]
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

translations = response[0]['translations']
translated_text = [translation['text'] for translation in translations]


# Create the output file name
output_file = f"translated_{translation_language}.txt"

# Write the translated content to the output file
with open(output_file, 'w') as file:
    file.write(translated_text[0])

print(f"Translation completed. Translated content saved to: {output_file}")