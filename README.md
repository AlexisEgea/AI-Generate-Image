# AI-Generate-Image

## Description 

This project use artificial intelligence technology to generate images.  
A user submits a request in the form of a prompt (= text message), and the model will generate an image based on it.  
The clearer the prompt, the more accurately the image will match your expectations.

- The `src` directory contains the project's source code.
- The `data` directory contains an Excel file with the project's history (prompts and image names) as well as the saved images in the "image" directory.

Here is a result of the project using the prompt `a magnificent baby dog`.
![Generated Image](data/image/image_2.jpg)

## Requirement

- Having Python3 and Pip installed on your machine.
- This project uses DALL-E 3 model from OpenAI, so you will need to have an account with funds to pay for each image created, as well as an API key.  
For more information: https://platform.openai.com/settings/profile. 

## Execution 

To get the project running on your machine, you need to install the libraries using the `requirement.txt` file.  
You can run the `installation-requirements.sh` script to install the following libraries:

- `openai` gives access to OpenAI models like GPT and DALL-E.
- `openpyxl` enables reading and writing (and more) of Excel files (.xlsx) in Python.
- `Pillow` is a library for opening, manipulating, and saving image files in various formats.
- `requests` simplifies sending HTTP requests and handling responses in Python.

Once the prerequisites are installed, you can run the `AI-Generate-Image.sh` script to execute the project.  
Follow the project instructions and have fun :)   

### On Ubuntu:

To execute a `.sh` Script:  
   1. Open a terminal.  
   2. Run the command `chmod +x script_name.sh` to make the script executable.  
   3. Execute the script by running `./script_name.sh`.  

Commands to run to make the project work:
1. Cloning the project to your machine
```sh
git clone https://github.com/AlexisEgea/AI-Generate-Image.git
```
2. Installing the prerequisites
```sh
chmod +x installation-requirements.sh
```
```sh
./installation-requirements.sh
```
3. Run the project
```sh
chmod +x AI-Generate-Image.sh
```
```sh
./AI-Generate-Image.sh
```

### On Windows:


Double-click on the `installation-requirements.sh` script, preferably with `Git Bash`, to install the prerequisites:"
```
installation-requirements.sh
```

Double-click on the `AI-Generate-Image.sh` script, preferably with `Git Bash`, to run the project:
```
AI-Generate-Image.sh
```
The `AI-Generate-Image.sh` script will return an error because of the executed Python command if you use `python ...` to execute a Python command. Please replace this line of code:
```sh
python3 -m main
```
with this one 
```sh
python -m main
```
Note that the current version of the project has been tested on Linux. If you encounter difficulties running the project, feel free to use an IDE (PyCharm, VS Code, or another), create a `venv` environment with the `requirements.txt` file, and execute the `main.py` file.

## Contact Information

 For inquiries or feedback, please contact me at [alexisegea@outlook.com](mailto:alexisegea@outlook.com).

## Copyright

© 2024 Alexis EGEA. All Rights Reserved.