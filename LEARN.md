# How does this project work ?
1. First you put your pages in the folder named folder
2. Then when you run the script, it goes through the pages folder to find the pages by using pathlib file
3. Script also opens the config.js as jsonFile then gets your Wi-Fi SSID etc.
4. After finding the pages, our script writes the basic boilerplate code to the result file which we opened in the 6th line of WebServerCreator.py
5. Right after the boilerplate our code searches for every file in the pages folder then writes their contents to result file (line by line expalnation is in the script file itself.)
6. Then script finished by adding the ending boilerplate codes to the end of our result file