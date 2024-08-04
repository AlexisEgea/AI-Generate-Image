
#!/bin/bash

echo "-----------------------------------------------------------------------------"
echo "|                          Installation Requirements                        |"
echo "| Author : Alexis EGEA                                                      |"
echo "-----------------------------------------------------------------------------"

echo "_____________________________________________________________________________"
echo "creation venv repository..."
python3 -m venv venv
echo "...done"
echo "_____________________________________________________________________________"
echo "activation venv..."
source venv/bin/activate #for linux
#venv\Scripts\activate #for window
echo "...done"
echo "_____________________________________________________________________________"
echo "installation requirement.txt"
pip install -r requirement.txt
echo "Done, project ready to be executed"

echo 
read -p "Press any key to close the terminal window"
