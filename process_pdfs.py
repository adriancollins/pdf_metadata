from PyPDF2 import PdfFileWriter, PdfFileReader
#process pdfs

#Input file list front find_pdfs.py
in_list = "PDF_list.txt"

#Output file names (note these will be overwritten is they already exist
buff_file = "buffer_list.txt"
out_file = "pdf_output.txt"
failed_files = "failed_files_output.txt"


#Initialise the files to clear existing content
f = open(failed_files,'w')
f.close()

f = open(out_file,'w')
f.close()



#read lines
with open(in_list) as f:
    content = f.readlines()


for i in range (0,len(content)):
    #initialize variables
    title_val = ''
    year_val = ''
    pdf_producer =''
    pdf_creator =''
    

    #fault tolerance - save additional paths
    f = open(buff_file,'w')
    for m in range (i,len(content)):
        f.write(content[m])
    f.close()


    curr_file = content[i].replace('\n', '')
    file_name_array = curr_file.split('/')
    file_name = file_name_array[len(file_name_array)-1]
    print (str(content[i]))

    try:
        input_PDF = PdfFileReader(curr_file)
        pages_val = str(input_PDF.getNumPages())
        docInfo = input_PDF.getDocumentInfo()
        title_val= docInfo.title
        if title_val is None:
            title_val = ''
        else:
            title_val = title_val.encode('utf-8')
            title_val = title_val.replace(',', ' ')

    except:
        #file locked
        pages_val = 'file locked'
        #write to file
        f = open(failed_files,'a')
        f.write(curr_file +'\n')
        f.close()

    
    try:
        docInfo2 = input_PDF.getXmpMetadata()
        date_val = docInfo2.xmp_modifyDate
        date_val = docInfo2.xmp_createDate
        
        date_val_split = str(date_val).split("-")
        year_val = date_val_split[0]
        pdf_producer =docInfo2.pdf_producer
        pdf_creator =docInfo2.xmp_creatorTool
        pdf_desc = docInfo2.dc_description
        pdf_key = docInfo2.pdf_keywords

        if pdf_producer is None:
            pdf_producer = ''
        else:
            pdf_producer = pdf_producer.encode('utf-8')

        if pdf_creator is None:
            pdf_creator = ''
        else:
            pdf_creator = pdf_creator.encode('utf-8') 


        
    except:
        year_val = 'unknown'
        pdf_producer ='unknown'
        pdf_creator ='unknown'
    


  

    out_str = curr_file + "|" +file_name + "|" + pages_val + "|" + title_val + "|" + year_val + "|" + str(pdf_producer) + "|"+ str(pdf_creator)
    f = open(out_file,'a')
    f.write(out_str+'\n')
    f.close()
    print(out_str)
