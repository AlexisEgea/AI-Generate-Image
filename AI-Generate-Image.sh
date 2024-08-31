
#!/bin/bash

# "-----------------------------------------------------------------------------"
# "|     © Execution Project Generation Image with OpenAI Dall-e-3 model       |"
# "| Author : Alexis EGEA                                                      |"
# "-----------------------------------------------------------------------------"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	PYTHON_CMD=python3
elif [[ "$OSTYPE" == "cygwin"* ]]; then
 	PYTHON_CMD=python3
else
	echo "Unsupported OS '$OSTYPE'"
	exit 1
fi

cd src/
$PYTHON_CMD -m main
cd ..

echo 
read -p "Press any key to close the terminal window"
