# Semi Auto Process

## Project - Sunshine Act Automation

### 1. Environment Setup
#### Prerequisite - install Python and Git

Open 'Command Prompt' and follow the instruction:

* Step 1:\
 Open Command prompt and choose the location you want to save the auto process.\
 For example, if you want save the file in the 'Sunshine Act' under 'Desktop', you can type 
```
cd Desktop\Sunshine Act
```
* Step 2:\
 clone the repo to your local, please copy and paste the following command in your command line
```
git clone https://github.com/Zili125935/semi_auto_process.git
cd semi_auto_process
pip install -r requirements.txt
```
*Remember to click 'enter'
* Step 3:\
Rename the input excel file to 'EXPORT.xlsx' \
copy the input excel file under folder 'semi_auto_process'\

* Step 4:\
Go back to Command, copy & paste the following command to run the script
```
python sunshine_run.py
```

### 2. Daily Use
* Step 1:\
Rename the input excel file to 'EXPORT.xlsx'\
copy the input excel file under folder 'semi_auto_process'\
**Please make sure rename new input excel file everytime you use this script!**

* Step 2:\
Open 'Command Prompt', copy paste & enter
```
cd Desktop\Sunshine Act\semi_auto_process
git pull
python sunshine_run.py
```
* Note -
Please note if the folder name is changed, you have to change the command as well.\
For example, if the 'Sunshine Act' has be changed to 'Sunshine', the first command will be 'cd Desktop\Sunshine\semi_auto_process'
