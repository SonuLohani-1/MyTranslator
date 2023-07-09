# .txt File Translator using AZURE REST API

## Video Demo: https://youtu.be/v-x9wmBBWIc

## Description:
This project is a **.txt file translator** that utilizes the *AZURE REST API* for translation. It allows you to translate text from one language to another, both from files and live input.

## Prerequisites
To use this project, you need to have the following:

- AZURE subscription with access to the Translation service (if you are a university student you can get your free $100 credit and other free services: [AZURE FOR STUDENTS](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjCgsTpkPf_AhVV-jgGHVTEAmcQFnoECAkQAQ&url=https%3A%2F%2Fazure.microsoft.com%2Fen-us%2Ffree%2Fstudents&usg=AOvVaw0PJ7vWwGI7uoSaSCh7R0_O&opi=89978449))

- Python installed on your machine

## Installation
1. Clone this repository to your local machine.
2. Install the required Python packages by running the following command:

```pip install -r requirements.txt```

## Configuration
1. Create a tranlate on AZURE and obtain your AZURE_KEY, endpoint, and location from the AZURE portal.
2. Open the `config.py` file and enter your AZURE subscription key, endpoint, and location in the respective variables.

## Usage
Run the `project.py` file with the following command:

python project.py [-f FILE] [-t TO]

- `-f FILE` (optional): Path to the input .txt file that you want to translate.
- `-t TO` (optional): The target language for translation. If not provided, the default language is English (en).
- (Note: you must provide at least one of the arguments for the proper working)

## Examples
1. Translate a text file:

```python project.py -f input.txt -t es```

This command translates the content of the `input.txt` file to Spanish and saves the translated text to `translated_es.txt`.

2. Live translation:

```python project.py -t fr```

This command allows you to enter text live in the terminal and translates it to French.

## Note
- The supported file format for translation is `.txt`.

Feel free to explore and modify the code according to your requirements. Happy translating!