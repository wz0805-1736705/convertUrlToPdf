# convertUrlToPdf
This tool can convert an url to pdf by passing a valid url and an expected output file name.

## First Time Use
1. If you need to install ```pip```, please see [here](https://www.geeksforgeeks.org/how-to-install-pip-in-macos/). If you need to install ```Python```, please see [here](https://www.python.org/downloads/macos/).
2. Locate to the folder of the tool<br>
```$ cd (YourFileLocation)/convertUrlToPdf```<br />
3. Set up virtual environment<br />
```$ virtualenv env```
4. Activate virtual environment<br />
```$ source env/bin/activate```
5. Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
6. Install required packages<br />
```$ pip install pdfkit```<br />
```$ pip install validators```

## Run tool
1. Locate to the folder of the tool<br>
```$ cd (YourFileLocation)/convertUrlToPdf```<br />
2. Activate virtual environment<br />
```$ source env/bin/activate```
3. Run the python code<br />
```$ python3 convertWebToPdf.py```
4. The terminal will require you to input an url. The url should start with <b>https://</b>, otherwise, the input is not valid.
5. The terminal will require you to input a file name
6. If convert successfully, the terminal will display <b>Convert Successfully</b>. Otherwise, it will say<b> Something went wrong. Please try again</b>
7. If convert successfully, you will be able to see the pdf file in the same folder.
8. Throwing errors does not mean that the conversion has failed, instead, some part of the webpage may not be supported by this tool and only part of the webpage has been converted.
9. Deactivate the virtual environment<br />
```$ deactivate```