# Raspberry Pi Code
### Initial setup
    Step 1. Check if the RPi is connected to OBD-II.
    Step 2. Run command "sudo rfcomm bind rfcomm0 00:1D:A5:03:E8:51"
                How to get the MAC Address: Run "bluetoothctl" and "devices" to retrieve it.
    Step 3. Run the python code "Main_4.py", output should be displaying after approximately 60 seconds.
    
### To-Do: (RPi)
    1. Connect GPIO Pins with Blind-spot symbols in the GUI
    
### Issues Encountered: 
    1. Some cars do not have all the requested OBD Codes for our GUI. (01 Honda Accord did not have FUEL_LEVEL command).

# Arduino Code
### Information
    The most functioning code as of now (2/28/2020) is in the "Multiple_Ultrasonic.ino".
    This .ino contains tested results of 4 ultrasonic sensors working simultaneously along with the accelerometer.
    
### To-Do: (Arduino)
    1. Implement the microwave sensor code (uses MPH rather than motion) into the "Multiple_Ultrasonic.ino" and test using all sensors.
    2. Fill in the portion of the code to turn the brake light relay on and off. (Relay takes a 5V input to switch a high voltage source on        and off, in our case, 12V).
    
### Issues Encountered:
    1. Having all the sensors connected to the Arduinos 5V output drew too much current causing the sensors to read incorrectly.
            A temporary fix is using a separate USB source for the 4 Ultrasonic sensors (The RED cable with jumper wire ends).
