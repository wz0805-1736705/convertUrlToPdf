import pdfkit
import validators

url = input("Url: (https://....)")
valid = validators.url(url)
while not valid:
    print("URL format incorrect!")
    url = input("Url: (https://....)")
    valid = validators.url(url)
output = input("File name: ")
while not output:
    print("File name cannot be empty!")
    output = input("File name: ")
if '.pdf' not in output:
    output = output + '.pdf'
if pdfkit.from_url(str(url), str(output)):
    print("Convert Successfully!")
else:
    raise Exception("Something went wrong. Please try again")