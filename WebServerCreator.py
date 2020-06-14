import pathlib, json

with open('config.json', 'r') as jsonFile:
    config = json.loads(jsonFile.read())

result = open("webserver.cpp","w+")

pages = []

# Writing required variables and seeting up library for result file
result.write(
'#include <Arduino.h>'
+'\n#include <ESP8266WebServer.h>'
+'\n\nconst char* ssid = '
+"\""+ config["SSID"] +"\"" 
+';\nconst char* password = ' 
+"\""+ config["Password"] +"\""
+';\n\nESP8266WebServer server('
+config["Port"] + ');\n\n\n'
)

# Searching for every file in pages folder.
try:
    for path in pathlib.Path('pages').iterdir():
        if path.is_file():
            if path.name.endswith('.html'): # Checking if file is a HTML file.
                currentFile = open(path, "a+") # Opening file
                pageName = currentFile.name.rsplit('\\')[1].rsplit('.')[0] # Getting file name without directory and "/".
                pages.append(pageName) # Adding file name to a list for final declaration.
                result.write("void "+ pageName +"(){\nchar *" + pageName + " = ") # Converting file to a char variable
                try:
                    x = 1
                    currentFile.seek(0)
                    fileLength = sum(1 for line in currentFile)
                    currentFile.seek(0)
                    for line in currentFile: # A loop for every line
                        strippedLine = line.strip() # Clearing empty lines
                        if strippedLine != "": # Checking if the line is empty
                            editedLine = strippedLine.replace("\"","\'")
                            result.write("\"" + editedLine)
                            currentLine = result.tell()
                            result.seek(currentLine)
                            if x == fileLength: # Checking if the line is the last line
                                result.write("\";\n\nserver.send(200, \"text/html\", "+ pageName +");\n}\n\n")
                            else: # If not, it won't add server.send(...).
                                result.write("\"\n")
                            x = x+1
                        else:
                            x = x+1
                            
                finally:
                    currentFile.close()
                    print(pageName + ' page is finished.')
            else:
                print("Skipped non HTML file")
finally:
    print("Proccess ended, Web Server complete.")

# Setup of result file
result.write(
'void setup() {'
+ '\n\tSerial.begin('
+ config["BaudRate"] + ');'
+ '\n\tdelay(10);'
+ '\n\tWiFi.begin(ssid,password);'
+ '\n\twhile(WiFi.status() != WL_CONNECTED){'
+ '\n\t\tSerial.print(\"Connection failed, trying again.\\n\");'
+ '\n\t\tdelay(500);'
+ '\n\t}'
+ '\n\tSerial.println(\"Connected Succesfully.\\n\");'
+ '\n\tserver.begin();'
+ '\n\tSerial.print("Server is live use http://");'
+ '\n\tSerial.print(WiFi.localIP());'
+ '\n\tSerial.print("/");'
+ '\n\n\tserver.begin();\n'
)

# Declare every page
for x in pages:
    result.write("\tserver.on("+ "\"/" + x + "\", " + x +");\n")
result.write("}\n\n\n")

# Loop of result file
result.write("void loop() {"
+ "\n\tserver.handleClient();"
+ "\n\tdelay(1000);"
+ "\n}")