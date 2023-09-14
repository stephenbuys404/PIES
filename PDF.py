#pdfkit
#https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.msvc2015-win64.exe
import os
import pdfkit
from pdfkit.api import configuration

def convert(link,name):
    filename='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    wkhtml_path=pdfkit.configuration(wkhtmltopdf=filename)
    pdfkit.from_url(link,name,configuration=wkhtml_path)

convert('https://www.google.com','sample.pdf')
