# CMPE195 MAST Group 28
## Luis Avila, Alex Gomez-Chavez, Darren Truong, Kevin Wong
## Raspberry Pi Code
### Initial setup
    Step 1. Check if the RPi is connected to OBD-II.
    Step 2. Run command "sudo rfcomm bind rfcomm0 00:1D:A5:03:E8:51"
                How to get the MAC Address: Run "bluetoothctl" and "devices" to retrieve it.
    Step 3. Run the python code "Main_4.py", output should be displaying after approximately 60 seconds.
    
### To-Do: (RPi)
- [x] Connect GPIO Pins with Blind-spot symbols in the GUI
- [x] Create a button for reversing (on/off)
    
### Issues Encountered: 
    1. Some cars do not have all the requested OBD Codes for our GUI. (01 Honda Accord did not have FUEL_LEVEL command).

## Arduino Code
### Initial setup
    The most functioning code as of now (2/28/2020) is in the "Multiple_Ultrasonic.ino".
    This .ino contains tested results of 4 ultrasonic sensors working simultaneously along with the accelerometer.
    
### To-Do: (Arduino)
- [x] Fill in the portion of the code to turn the brake light relay on and off. (Relay takes a 5V input to switch a high voltage source on and off, in our case, 12V). Since we are making the brake light blink, we will need non-interferring delays between on and off. We also need to make sure it only blinks a few times after heavy braking has been detected.
- [x] Attempt to create and test the addition of only reading backup sensors on GPIO input. So we can add a switch or signal wire input in the future.

# Entire Project
### Overall To-Do:
- [x] 3D-Model an enclosure to fit the Arduino, 4 JSN-SR04T Modules, and 4-Channel Relay. (Mounting holes and wire holes). [Link](https://am22.mediaite.com/tms/cnt/uploads/2020/01/babyyoda.jpg)
- [x] 3D-Model an enclosure for the Microwave sensor (retrieve dimensions first).
- [x] Create custom Dupont connectors for each sensor (ex. JSN-SR04T, SEN0192 Microwave Sensor, Speaker Wire, Relays).
- [x] Find a long, 2-core (or 4) insulated wire for connecting the Arduino and RPi (Microwave sensor info). Should solder the waterproof connector between them. 
- [x] Add a button (or 12V input) to signal reversing and reading of backup sensors.
- [x] Mount sensor on test vehicle. (Drill holes for Ultrasonic, Mount Microwave to sides of the bumper, Route cables to the trunk, splice brake light wires).
- [x] Create the video demo.
