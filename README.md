# ESP8266WebServer Creator
You can create your WebServers with ease by using this script.

## How it Works ?
* It takes every HTML file in `pages` folder and adds them into a .cpp file in a proper way.
* Then you can upload it to your Arduino, NodeMCU etc...

## Before Using !
* Don't use index.html as a file name because it creates a problem, use anything other instead.
* I tested the results with PlatformIO so there might be problems when using Arduino IDE you can report them by using `Issues`.

## How to Use ?
* Put your HTML files in `pages` folder.
* Modify config.json
* Run the script and that's it.

## Config.json
* SSID = Your WiFi Name
* Password = Your WiFi Password
* BaudRate = Desired BaudRate
* Port = Server Port

## Example Result
You can see example result from [this page](https://gist.github.com/yussufjpg/10c04b4c92bc69da3b224e97a80e2bfa)