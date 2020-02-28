# Raspberry Pi Code
### Initial setup
    Step 1. Check if the RPi is connected to OBD-II.
    Step 2. Run command "sudo rfcomm bind rfcomm0 (Insert MAC Address of obd-scanner)
            How to get the MAC Address: Run "bluetoothctl" and "devices" to retrieve it.
    Step 3. Run the python code "Main_4.py", output should be displaying after approximately 60 seconds.
