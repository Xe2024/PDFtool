# converting the pdf to image
from pdf2image import convert_from_path
# Store Pdf with convert_from_path function
images = convert_from_path('C:/Users/COMPUTER/Downloads/Money And Credit_Shobhit Nirwan.pdf', poppler_path = r'C:\Program Files\poppler-24.08.0\Library\bin')
import PyPDF2

pdfList =[]
for i in range(len(images)):
  
      # Save pages as images in the pdf


    # convert to greyscale
    from PIL import Image
    import PIL.ImageOps  
     # Op
    # print("Successfully made pdf file")
    # Save the grayscale image

    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')en the image
    image = images[i]

    # Convert the image to grayscale
    image = image.convert("L")
    inverted_image = PIL.ImageOps.invert(image)

    # converting back to pdf
    import img2pdf
    import os
    
    inverted_image.save(f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/inverted_image{i}.jpg") 
    inverted_img_path = f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/inverted_image{i}.jpg"
    with Image.open(inverted_img_path) as finalimg:
        pdf = img2pdf.convert(finalimg.filename)
        with open( f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/pdfs/pdf{i}.pdf" , "wb") as file:
            file.write(pdf)
            print(f"converted {finalimg} to pdf{i}")
            pdfList.append(f"pdf{i}")
    
    
   


    # with open(r"C:\Users\COMPUTER\Desktop\PDFtools\invertColor\finalPDF\final.pdf", "wb") as f:
    #   f.write(img2pdf.convert([open(f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/{i}", "rb") for i in os.listdir('C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/') if i.endswith(".jpg")]))


# os.chdir(r"C:\Users\COMPUTER\Desktop\PDFtools\invertColor\pdfs")
# pdfs = os.listdir()
# pdfs.sort()

pdfMerge = PyPDF2.PdfMerger()

# loop through each pdf page
print(pdfList)
for pdf in pdfList:
  print(pdf)
  # open each pdf
  with open(f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/pdfs/{pdf}.pdf", 'rb') as pdfFile:
    # merge each file
    pdfMerge.append(PyPDF2.PdfReader(pdfFile))

# write the merged pdf 
pdfMerge.write(r'C:\Users\COMPUTER\Desktop\PDFtools\invertColor\finalPDF\final.pdf')

# download the final pdf
# files.download('merged.pdf')