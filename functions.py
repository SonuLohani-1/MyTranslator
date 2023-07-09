import requests, uuid, json, argparse, sys, os
import langcodes

def main():
    # get credentials
    credentials = get_Credentials()
    key = credentials["key"]
    endpoint = credentials["endpoint"]
    location = credentials["location"]

    # If program is run without any command-line arguments
    if len(sys.argv) == 1:
        sys.exit("Usage: python project.py [-f  FILE] [-t TO] \n MISSING FILE AND LANGUAGE!")

    #parsing the arguments to get file and language information
    try:
        parsed_data = parse_arguments()
        File = parsed_data["File"]
        if File != None and os.path.splitext(File)[1] != ".txt":
            sys.exit("The only supported file format is \".txt\"")
        translation_language = parsed_data["translation_language"]
        if File is None:
            while True:
                try:
                    print(live_translator(key, endpoint, location, translation_language))
                except EOFError:
                    print("\nBye, Have a nice day!")
                    return

        else:
            print(file_translator(key, endpoint, location, File, translation_language))

    except KeyError:
        sys.exit("Usage: python project.py [-f  FILE] [-t TO]")

    # When the language name couldn't be resolved
    except LookupError:
        sys.exit("UNRECOGNIZED/INVALID LANGUAGE")

    # When File provided doesn't exist
    except FileNotFoundError:
        sys.exit("FILE DOESN'T EXIST")


def get_Credentials():
    from config import AZURE_KEY, endpoint, location
    return {"key": AZURE_KEY, "endpoint": endpoint, "location" : location}

def parse_arguments():
    # Creating an argument parser
    parser = argparse.ArgumentParser(description="Tranlate text from one language to another")
    parser.add_argument("-f", "--file", help='Path to the input file')
    parser.add_argument("-t", "--to", help = "translation language")
    args = parser.parse_args()

    #getting translation language and input file from arguments
    input_file = args.file
    translation_language = args.to

    # if the language is not given return the default language 'en'
    if translation_language is None:
        translation_language_code = "en"
    else:
        translation_language_code = langcodes.find(translation_language.lower()).language
    return {"File" : input_file, "translation_language" : translation_language_code}

def file_translator(key, endpoint, location, File, translation_language):
    with open(File, 'r') as file:
        text = file.read()
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': [translation_language]
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
    return f"Translation completed. Translated content saved to: {output_file}"

def live_translator(key, endpoint, location, translation_language="en"):
    text = input("Text: ")
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': [translation_language]
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
    return translated_text;

if __name__ == "__main__":
    main()