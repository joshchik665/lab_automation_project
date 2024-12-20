# Lab Automation

By: Josh Chik

This project provides various tool to remotely control lab instruments. It includes a module that handels all things related to controlling the instrument, a customizable GUI with powerful features, and a setup wizard GUI that allows for the easy configuring of new or existing devices. 

## Setup

To setup the environment use : > conda env create -f environment.yml 
To install all required packages and modules use: > pip install -r requirements.txt

## GUI User Guide

To control an instrument with the GUI, all you need to do is run the main.py file and enter the IP address of the instrument you want to control in the dialog that pops up. It will then try to connect to the instrument at that IP address. It will then try to identify the type of instrument it is connected to by querying the IDN of that instrument. If the intrument type is in its library if devices, it will open the GUI for that intrument. You can also select a premade config file to load directly into intead of entering an IP address. This will connect to the IP address in the config file and then set all the setting.

See the Setup Wizard Guide for how to add a new instrument type.

By default, the GUI will have a few default buttons. These include:
1. The "Load Config" and "Save Config" buttons allow you to save and then reload all of the current settings
2. The "Apply All Settings" button will try to apply all of the settings on the window

## Module User Guide

In the Device dirctory, there is where all the modules that handle communication with the instruments are. The GUI uses these to control the instrument. You can also use the module separate from the GUI.

In the module there is the Settings manager, with this class, you can easily control the instrument. 

## Setup Wizard Guide

