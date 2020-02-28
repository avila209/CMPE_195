# Raspberry Pi Code
### Initial setup
    Step 1. Check if the RPi is connected to OBD-II.
    Step 2. Run command "sudo rfcomm bind rfcomm0 00:1D:A5:03:E8:51"
                How to get the MAC Address: Run "bluetoothctl" and "devices" to retrieve it.
    Step 3. Run the python code "Main_4.py", output should be displaying after approximately 60 seconds.
    
### To-Do: (RPi)
    [ ] Connect GPIO Pins with Blind-spot symbols in the GUI
    
### Issues Encountered: 
    1. Some cars do not have all the requested OBD Codes for our GUI. (01 Honda Accord did not have FUEL_LEVEL command).

# Arduino Code
### Information
    The most functioning code as of now (2/28/2020) is in the "Multiple_Ultrasonic.ino".
    This .ino contains tested results of 4 ultrasonic sensors working simultaneously along with the accelerometer.
    
### To-Do: (Arduino)
    1. Implement the microwave sensor code ("Microwave_Sensor_2.ino", uses MPH rather than motion) into the "Multiple_Ultrasonic.ino" and test using all sensors.
    2. Fill in the portion of the code to turn the brake light relay on and off. (Relay takes a 5V input to switch a high voltage source on and off, in our case, 12V).
    3. Attempt to create and test the addition of only reading backup sensors on GPIO input. So we can add a switch or signal wire input in the future.
    
### Issues Encountered:
    1. Having all the sensors connected to the Arduinos 5V output drew too much current causing the sensors to read incorrectly.
            A temporary fix is using a separate USB source for the 4 Ultrasonic sensors (The RED cable with jumper wire ends).

# Entire Project
### Overall To-Do:
    1. 3D-Print 4 JSN-SR04T Enclosures. [Link](https://www.thingiverse.com/thing:3007089)
    2. 3D-Model an enclosure to fit the Arduino, 4 JSN-SR04T Modules, and 4-Channel Relay. (Mounting holes and wire holes).
    3. 3D-Model an enclosure for the Microwave sensor (retrieve dimensions first).
    4. Create custom Dupont connectors for each sensor (ex. JSN-SR04T, SEN0192 Microwave Sensor, Speaker Wire).
    5. Find a long, 2-core (or 4) insulated wire for connecting the Arduino and RPi (Microwave sensor info). Should solder the waterproof connector between them. 
    6. Find an LED Light indicator for Blind Spot (Modularity - if user does not want/need the screen and RPi).
       Example: [KIA Lights](https://www.ebay.com/i/183941072754?chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=183941072754&targetid=874450542391&device=c&mktype=pla&googleloc=9032168&poi=&campaignid=9343999437&mkgroupid=103102736148&rlsatarget=aud-762207186714:pla-874450542391&abcId=1139336&merchantid=101492499&gclid=Cj0KCQiAkePyBRCEARIsAMy5SctQ5NckdIsExAfQYjG4616pFNezB2RSsZuSuKeKJnsuPxd1MI_JtQ4aAjNPEALw_wcB)
    7. Add a button (or 12V input) to signal reversing and reading of backup sensors.
    7. Mount sensor on test vehicle. (Drill holes for Ultrasonic, Mount Microwave to sides of the bumper, Route cables to the trunk, splice brake light wires).
