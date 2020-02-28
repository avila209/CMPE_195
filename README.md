# Raspberry Pi Code
### Initial setup
    Step 1. Check if the RPi is connected to OBD-II.
    Step 2. Run command "sudo rfcomm bind rfcomm0 00:1D:A5:03:E8:51"
            How to get the MAC Address: Run "bluetoothctl" and "devices" to retrieve it.
    Step 3. Run the python code "Main_4.py", output should be displaying after approximately 60 seconds.
