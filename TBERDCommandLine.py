"""TBERDCommandLine.py:
A sample command line interface for the T-BERD 5800
Dependencies:
TBERD5800Controls (dependency: TBERDCommandTypes)"""
from TBERD5800Controls import *






#When DEBUG=True, uses *REM VISIBLE ON (for debugging only)
#Otherwise, when DEBUG is False, uses *REM command
DEBUG=False

#START MAIN
#Get the ip address and attempt to connect
ipaddr=input("Please enter the ip address of the TB5800 to connect:\n")
try:
    tb1=TBERD5800Controls(targetip=ipaddr, timeout=10, debug=DEBUG)
    tb1.connect()
except Exception as e:
    print(f"Did not connect to TB5800 Correctly: Exception {e}")
while not tb1.isConnected:
    #Attempt to connect again
    ipaddr=input("Please enter the ip address of the TB5800 to connect:\n")
    try:
        tb1=TBERD5800Controls(targetip=ipaddr, timeout=10, debug=DEBUG)
        tb1.connect()
    except Exception as e:
        print(f"Did not connect to TB5800 Correctly: Exception {e}")
writelog("Entering Remote mode.")
tb1.setRemoteOn()
time.sleep(1)
#Bring up app selection screen automatically after connecting to remote   
#Will automatically reconnect if necessary
try:
    tb1.runCommand("MULTIAPP")
except Exception as e:
    print(f"Start Command did not run: Exception {e}")

notExit=True
while notExit:
    #Prompt for command and then format it
    activeapp=tb1.getActiveApp()
    if activeapp is None:
        print("No app currently active.")
    elif isinstance(activeapp, Application):
        print(f"Active App: {activeapp.getappname()}, Port{activeapp.getPort()}")
    else:
        print("Error: getActiveApp returned wrong type")
    cmdval=input("Enter a command or enter \"HELP\" for help:\n")
    try:
        if tb1.runCommand(cmdval) == "EXIT":
            notExit=False
    except Exception as e:
        print(f"Command did not run: Exception {e}")
    
"""
Any question about the script, please contact Brad Sicotte at 
email: bsicotte@teracomm.com
"""
        
