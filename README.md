# pdf_metadata
Python script that uses PyPDF2 to interrogate a directory to catalog the meta data of all available PDF files.

## Prerequisites
Install the following to use this project.
* Python 3
* PyPDF2 `pip3 install PyPDF2`

## Use
Two scripts are included in this repo along with test data. The test data is a dummy directory structure containing a number of PDF files. Note, these PDF files have been built from sections of [R Programming for Data Science](https://bookdown.org/rdpeng/rprogdatascience/).
1. Run `find_pdf.py` to create a text file containing the paths of each PDF in the directory specified by the variable `root_directory`. The script recursively checks each folder to find every PDF.
2. Run `process_pdfs.py` to generate a text file containing all the available metadata for each PDF discovered in `find_pdf.py`.
